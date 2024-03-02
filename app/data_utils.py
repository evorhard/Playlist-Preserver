import math
import requests

from io import BytesIO
from time import sleep
from typing import Dict

from celery import current_app as celery_app

# Local imports
from spotify_interaction import get_playlist_details


def get_all_pages(access_token: str, playlist_id: str, total: int) -> Dict:
    number_of_pages = math.ceil(total / 50)
    aggregated_data = {"items": []}

    for page in range(number_of_pages):
        sleep(1)

        headers = {"Authorization": f"Bearer {access_token}"}
        offset = page * 50  # Calculate the correct offset for each page

        response = requests.get(
            f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?limit=50&offset={offset}",
            headers=headers,
        )
        page_data = response.json()

        aggregated_data["items"].extend(page_data["items"])

    return aggregated_data


def clean_json(data: Dict) -> Dict:
    track_list = ""

    for item in data["items"]:
        track_list += f"{item['track']['artists'][0]['name']} - {item['track']['album']['name']}\n"

    return track_list


@celery_app.task(bind=True)
def download_playlist_task(
    self, access_token: str, playlist_id: str, playlist_name: str
):
    playlist_data = get_playlist_details(access_token, playlist_id)
    if playlist_data["total"] > 50:
        playlist_data = get_all_pages(access_token, playlist_id, playlist_data["total"])

    clean_data = clean_json(playlist_data)

    return clean_data
