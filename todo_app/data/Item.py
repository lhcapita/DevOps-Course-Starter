
from datetime import datetime, date

class Item:
    def __init__(self, id, name, status, desc, due):
        self.id = id
        self.name = name
        self.status = status
        self.desc = desc
        self.due = due

    @classmethod
    def from_db_row(cls, row):
        due = row["due"]
        if(due != None):
            due = datetime.strptime(due, '%m/%d/%Y')
        return cls(row["_id"], row["name"], row["status"], row["desc"], due)