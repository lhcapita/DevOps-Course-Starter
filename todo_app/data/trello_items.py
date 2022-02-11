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

def get_trello_lists():

    board_id = os.getenv("TRELLO_BOARD_ID")
    key = os.getenv("TRELLO_API_KEY")
    token = os.getenv("TRELLO_API_TOKEN")

    url = f"https://api.trello.com/1/boards/{board_id}/lists/"

    headers = {
        "Accept": "application/json"
    }

    query = {
        "fields": "name,id",
        "key": key,
        "token": token
    }

    response = requests.get(url, headers=headers, params=query)

    lists = response.json()


    return lists

def add_trello_item(title):

    board_id = os.getenv("TRELLO_BOARD_ID")
    key = os.getenv("TRELLO_API_KEY")
    token = os.getenv("TRELLO_API_TOKEN")

    idList = get_trello_lists()[0]["id"]

    url = "https://api.trello.com/1/cards/"

    headers = {
        "Accept": "application/json"
    }

    query = {
        "name": title,
        "idList": idList,
        "key": key,
        "token": token
    }

    response = requests.post(url, headers=headers, params=query)

    new_card = response.json()

    new_card_id = new_card["id"]

    return get_trello_item(new_card_id)
