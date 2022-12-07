import pymongo
import os
from todo_app.data.Item import Item

#from todo_app.data.Item import Item

#ID Title 	Status 	Description 	Due Date

class DbHandler:
    def __init__(self):
        connid = os.environ.get("DB_CONNECTION_STRING")
        db_name = os.environ.get("DB_NAME_ITEMS")

        self.client = pymongo.MongoClient(connid)
        self.db_items = self.client[db_name]
        self.collection = self.db_items.items_collection
    
    def GetLists(self):
        return ["Not Started", "In Progress", "Peer Review", "On Hold", "Completed"]

    def GetItems(self):
        posts = self.db_items.posts
        resp = posts.find()
        items = []
        for i in resp:
            item = Item(i["_id"], i["name"], i["status"], i["desc"], i["due"])
            items.append(item)
        return items

    def GetItem(self, id):
        posts = self.db_items.posts
        return posts.find_one({"_id": id})

    def AddItem(self, title, desc, due):
        post = {"name": title,
            "desc": desc,
            "status": "Not Started",
            "due": due}

        posts = self.db_items.posts
        post_id = posts.insert_one(post).inserted_id
        return None

    def UpdateItem(self, item:Item):
        obj = {"_id": item.id}
        new_vals = { "$set": { "name": item.name,
                                "desc":  item.desc,
                                "status": item.status,
                                "due": item.due} }
        posts = self.db_items.posts
        posts.update_one(obj, new_vals)
        return None

    def DeleteItem(self, id):
        query = {"_id": id}
        posts = self.db_items.posts
        posts.delete_one(query)
        return None
