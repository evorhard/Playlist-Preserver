from typing import Dict


def clean_json(data: Dict) -> Dict:
    track_list = ""

    for item in data["items"]:
        track_list += f"{item['track']['artists'][0]['name']} - {item['track']['album']['name']}\n"

    return track_list
