import requests
import os
import json


def get_trello_items():

    board_id = os.getenv("TRELLO_BOARD_ID")
    key = os.getenv("TRELLO_API_KEY")
    token = os.getenv("TRELLO_API_TOKEN")

    url = f"https://api.trello.com/1/boards/{board_id}/lists/"

    headers = {
        "Accept": "application/json"
    }

    query = {
        'cards': 'open',
        "key": key,
        "token": token
    }

    response = requests.get(url, headers=headers, params=query)

    lists = response.json()

    items = []
    
    for l in lists:
        status = l["name"]
        cards = l["cards"]

        for card in cards:
            card_id = card["id"]
            card_name = card["name"]
            item = {"id": card_id, "status": status, "title": card_name}
            items.append(item)

    return items

def get_trello_item(id):
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    items = get_trello_items()
    return next((item for item in items if item['id'] == id), None)