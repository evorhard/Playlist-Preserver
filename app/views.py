import json

from urllib import parse as urllibparse

from datetime import datetime
from flask import (
    Blueprint,
    jsonify,
    redirect,
    session,
    render_template,
    request,
    send_file,
    url_for,
)
from loguru import logger

# Local imports
from config import (
    API_BASE_URL,
    AUTHORIZATION_URL,
    CLIENT_ID,
    CLIENT_SECRET,
    REDIRECT_URI,
    SCOPE,
    TOKEN_URL,
)
from spotify_authorization import (
    exchange_code_for_token,
    get_playlist_details,
    get_user_information,
    get_user_playlist,
    refresh_token,
)
from data_utils import clean_json

views_blueprint = Blueprint("views", __name__)


@views_blueprint.route("/")
def index():
    return render_template("login.html")
    return "Welcome to my Spotify App <a href='/login'>Login with Spotify</a>"


@views_blueprint.route("/login")
def login():
    """Initial login screen

    Returns:
        redirect -- Redirects to authorization screen
    """
    login_url_parameters = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "scope": SCOPE,
        "redirect_uri": REDIRECT_URI,
        "show_dialog": True,
    }

    authorization_url = (
        f"{AUTHORIZATION_URL}?{urllibparse.urlencode(login_url_parameters)}"
    )

    return redirect(authorization_url)


@views_blueprint.route("/callback")
def callback():
    """Callback

    Returns:
        redirect -- Redirects to getting the user id page
    """
    if "error" in request.args:
        return jsonify({"error": request.args["error"]})

    if "code" in request.args:
        token_info = exchange_code_for_token(
            request.args["code"], CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, TOKEN_URL
        )

        session["access_token"] = token_info["access_token"]
        session["refresh_token"] = token_info["refresh_token"]
        session["expires_at"] = datetime.now().timestamp() + token_info["expires_in"]

        return redirect("/user-id")


@views_blueprint.route("/user-id")
def user_information():
    if "access_token" not in session:
        return redirect("/login")

    if datetime.now().timestamp() > session["expires_at"]:
        return redirect("/refresh-token")

    user_information = get_user_information(session["access_token"])

    session["user_id"] = user_information.id
    session["display_name"] = user_information.display_name

    return redirect("/playlists")


@views_blueprint.route("/playlists")
def get_playlists():
    if "user_id" not in session:
        return redirect("/login")

    playlists_data = get_user_playlist(
        access_token=session["access_token"], user_id=session["user_id"]
    )

    playlists = playlists_data.get("items", [])

    return render_template(
        "playlists.html", playlists=playlists, display_name=session["display_name"]
    )


@views_blueprint.route("/playlist/<playlist_id>")
def playlist_details(playlist_id):
    access_token = session.get("access_token")
    user_id = session.get("user_id")

    if not access_token or not user_id:
        return redirect(url_for("login"))

    playlist_data = get_playlist_details(access_token, user_id, playlist_id)

    return jsonify(playlist_data)


@views_blueprint.route("/download_playlist/<playlist_id>")
def download_playlist(playlist_id):
    access_token = session.get("access_token")
    user_id = session.get("user_id")

    if not access_token or not user_id:
        return redirect(url_for("login"))

    playlist_data = get_playlist_details(access_token, user_id, playlist_id)

    cleaned_json = clean_json(playlist_data)

    from io import BytesIO

    file_obj = BytesIO(json.dumps(playlist_data).encode("utf-8"))

    return send_file(
        file_obj, as_attachment=True, download_name=f"playlist_{playlist_id}.json"
    )


@views_blueprint.route("/refresh-token")
def refresh_token():
    if "refresh_token" not in session:
        return redirect("/login")

    if datetime.now().timestamp() > session["expires_at"]:
        new_token_info = refresh_token(
            session["refresh_token"], CLIENT_ID, CLIENT_SECRET, TOKEN_URL
        )

        session["access_token"] = new_token_info["access_token"]
        session["expires_at"] = (
            datetime.now().timestamp() + new_token_info["expires_in"]
        )

    return redirect("/playlists")
