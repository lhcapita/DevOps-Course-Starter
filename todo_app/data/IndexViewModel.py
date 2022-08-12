from todo_app.data.Item import Item
from todo_app.data.trello_items import get_trello_lists

class ViewModel:
    def __init__(self, items, lists, errored):
        self._items = items
        self._errored = errored
        self._sorted_items = {}
        self._lists = lists        
        self._sort_items()

    def _sort_items(self):
        trello_lists = self.trello_lists

        for trello_list in trello_lists:
            list_name = trello_list["name"]
            self._sorted_items[list_name] = []

        #sort items into correct list
        for item in self._items:
            self._sorted_items[item.status].append(item)

    @property
    def sorted_items(self):
        self._sort_items()
        return self._sorted_items

    @property
    def items(self):
        return self._items

    @property
    def trello_lists(self):
        return self._lists

    @property
    def errored(self):
        return self._errored
        
    @property 
    def not_started_items(self):
        return self.sorted_items["Not Started"]
        
    @property 
    def in_progress_items(self):
        return self.sorted_items["In Progress"]
        
    @property 
    def peer_review_items(self):
        return self.sorted_items["Peer Review"]
        
    @property 
    def on_hold_items(self):
        return self.sorted_items["On Hold"]
        
    @property 
    def completed_items(self):
        return self.sorted_items["Completed"]
