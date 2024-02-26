import pytest

from contextlib import contextmanager
from datetime import datetime
from flask import template_rendered, session
from urllib import parse

from unittest.mock import patch


# Local imports
from app import create_app


@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client


@contextmanager
def captured_templates():
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record)

    try:
        yield recorded
    finally:
        template_rendered.disconnect(record)


def test_index_route(client):
    response = client.get("/")

    assert response.status_code == 200
    assert "Welcome to Disc List Scout" in response.text


def test_login_route_with_mocked_config(client, mocker):
    mocker.patch("views.CLIENT_ID", "test_client_id")
    mocker.patch("views.SCOPE", "test_scope")
    mocker.patch("views.REDIRECT_URI", "http://test_redirect_uri")

    response = client.get("/login")
    expected_url = "https://accounts.spotify.com/authorize?client_id=test_client_id&response_type=code&scope=test_scope&redirect_uri=http%3A%2F%2Ftest_redirect_uri&show_dialog=True"

    assert response.status_code == 302
    assert response.location == expected_url


def test_callback_with_error(client):
    response = client.get("/callback?error=access_denied")

    assert response.status_code == 200
    assert b"access_denied" in response.data


@patch("views.exchange_code_for_token")
def test_callback_with_code(mock_exchange_code, client):
    mock_exchange_code.return_value = {
        "access_token": "mock_access_token",
        "refresh_token": "mock_refresh_token",
        "expires_in": 3600,
    }

    response = client.get("/callback?code=some_auth_code")

    assert response.status_code == 302
    assert response.location == "/user-id"

    with client.session_transaction() as session:
        assert session["access_token"] == "mock_access_token"
        assert session["refresh_token"] == "mock_refresh_token"
        assert session["expires_at"] > datetime.now().timestamp()


def test_callback_redirects_to_user_id(client, mocker):
    mock_token_info = {
        "access_token": "mock_access_token",
        "refresh_token": "mock_refresh_token",
        "expires_in": 3600,
    }

    mocker.patch("views.exchange_code_for_token", return_value=mock_token_info)

    response = client.get("/callback?code=some_valid_code")

    assert response.status_code == 302
    assert response.location == "/user-id"


def test_get_playlists_redirects_when_not_logged_in(client):
    response = client.get("/playlists", follow_redirects=False)

    assert response.status_code == 302
    assert response.location == "/login"


def test_get_playlists_calls_get_user_playlist(client, mocker):
    with client.session_transaction() as session:
        session["user_id"] = "test_user_id"
        session["access_token"] = "test_access_token"
        session["display_name"] = "Test User"

    mock_get_user_playlist = mocker.patch(
        "views.get_user_playlist", return_value={"items": []}
    )

    client.get("/playlists")

    mock_get_user_playlist.assert_called_once_with(
        access_token="test_access_token", user_id="test_user_id"
    )


def test_get_playlists_updates_session_with_playlist_names(client, mocker):
    with client.session_transaction() as session:
        session["user_id"] = "test_user_id"
        session["access_token"] = "test_access_token"
        session["display_name"] = "Test User"

    mocked_playlists_data = {
        "items": [{"id": "1", "name": "Playlist 1"}, {"id": "2", "name": "Playlist 2"}]
    }
    mocker.patch("views.get_user_playlist", return_value=mocked_playlists_data)

    client.get("/playlists")

    with client.session_transaction() as sess:
        assert sess["playlist_names"] == {"1": "Playlist 1", "2": "Playlist 2"}


def test_get_playlists_renders_correct_template(client, mocker):
    with client.session_transaction() as session:
        session["user_id"] = "test_user_id"
        session["access_token"] = "test_access_token"
        session["display_name"] = "Test User"

    mocked_playlists_data = {"items": []}
    mocker.patch("views.get_user_playlist", return_value=mocked_playlists_data)

    with client.application.app_context():
        with captured_templates() as templates:
            client.get("/playlists")

            assert len(templates) == 1

            template, context = templates[0]

            assert template.name == "playlists.html"
            assert context["display_name"] == "Test User"
            assert "playlists" in context
