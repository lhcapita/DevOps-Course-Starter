
from datetime import datetime

class Item:
    def __init__(self, id, name, status, desc, due):
        self.id = id
        self.name = name
        self.status = status
        self.desc = desc
        self.due = due

    @classmethod
    def from_trello_card(cls, card, list):
        due = card['due']
        if(due != None):
            due = datetime.strptime(due, '%Y-%m-%dT%H:%M:%S.%fZ')
            due = due.date()
        return cls(card['id'], card['name'], list['name'], card['desc'], due)