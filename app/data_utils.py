from typing import Dict


def clean_json(data: Dict) -> Dict:
    for item in data["items"]:
        item["track"].pop("available_markets", None)
        item["track"]["album"].pop("images", None)
        item["track"]["album"].pop("available_markets", None)

    return data
