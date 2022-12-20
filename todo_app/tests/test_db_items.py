from todo_app.data.IndexViewModel import ViewModel
from todo_app.data.Item import Item



def generate_dummy_items():
    items = [
        Item('id', 'Item 1', 'Not Started', 'description', None),
        Item('id2', 'Item 9', 'Not Started', 'description', None),
        Item('id3', 'Item 10', 'Not Started', 'description', None),
        Item('id4', 'Item 5', 'In Progress', 'description', None),
        Item('id5', 'Item 7', 'In Progress', 'description', None),
        Item('id6', 'Item 4', 'Peer Review', 'description', None),
        Item('id7', 'Item 6', 'Peer Review', 'description', None),
        Item('id8', 'Item 2', 'On Hold', 'description', None),
        Item('id9', 'Item 3', 'Completed', 'description', None)
    ]
    return items
def generate_dummy_lists():
    db_lists = [
        "Not Started",
         "In Progress",
         "Peer Review",
         "On Hold",
         "Completed"
    ]
    return db_lists

class TestTodo:
    
    @staticmethod
    def test_db_items_not_started():
    
        # Arrange
        items = generate_dummy_items()
        db_lists = generate_dummy_lists()
        view_model = ViewModel(items, db_lists, True)
    
        # Act
        not_started_items = view_model.not_started_items
    
        # Assert
        assert "Item 1" == not_started_items[0].name
        assert "Item 9" == not_started_items[1].name
        assert "Item 10" == not_started_items[2].name
    
    @staticmethod
    def test_db_items_in_progress():
    
        # Arrange
        items = generate_dummy_items()
        db_lists = generate_dummy_lists()
        view_model = ViewModel(items, db_lists, True)
    
        # Act
        in_progress_items = view_model.in_progress_items
    
        # Assert
        assert "Item 5" == in_progress_items[0].name
        assert "Item 7" == in_progress_items[1].name
    
    @staticmethod
    def test_db_items_peer_review():
    
        # Arrange
        items = generate_dummy_items()
        db_lists = generate_dummy_lists()
        view_model = ViewModel(items, db_lists, True)
    
        # Act
        peer_review_items = view_model.peer_review_items
    
        # Assert
        assert "Item 4" == peer_review_items[0].name
        assert "Item 6" == peer_review_items[1].name
    
    @staticmethod
    def test_db_items_on_hold():
    
        # Arrange
        items = generate_dummy_items()
        db_lists = generate_dummy_lists()
        view_model = ViewModel(items, db_lists, True)
    
        # Act
        on_hold_items = view_model.on_hold_items
    
        # Assert
        assert "Item 2" == on_hold_items[0].name
    
    @staticmethod
    def test_db_items_completed():
    
        # Arrange
        items = generate_dummy_items()
        db_lists = generate_dummy_lists()
        view_model = ViewModel(items, db_lists, True)
    
        # Act
        completed_items = view_model.completed_items
    
        # Assert
        assert "Item 3" == completed_items[0].name
    
    @staticmethod
    def test_db_items_sorted():
    
        # Arrange
        items = generate_dummy_items()
        db_lists = generate_dummy_lists()
        view_model = ViewModel(items, db_lists, True)
    
        # Act
        sorted_items = view_model.sorted_items
    
        # Assert
        assert "Item 1" == sorted_items["Not Started"][0].name
        assert "Item 9" == sorted_items["Not Started"][1].name
        assert "Item 10" == sorted_items["Not Started"][2].name
        assert "Item 5" == sorted_items["In Progress"][0].name
        assert "Item 7" == sorted_items["In Progress"][1].name
        assert "Item 4" == sorted_items["Peer Review"][0].name
        assert "Item 6" == sorted_items["Peer Review"][1].name
        assert "Item 2" == sorted_items["On Hold"][0].name
        assert "Item 3" == sorted_items["Completed"][0].name
