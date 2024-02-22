import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client


def test_index_route(client):
    response = client.get("/")

    assert response.status_code == 200
    assert "Welcome to Disc List Scout" in response.text


def test_login_route(client):
    response = client.get("/login", follow_redirects=True)

    assert response.status_code == 200
    assert b"accounts.spotify.com" in response.data
