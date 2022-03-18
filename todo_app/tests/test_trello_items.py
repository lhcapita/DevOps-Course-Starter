from todo_app.data.trello_items import get_trello_items, get_trello_lists
from todo_app.data.IndexViewModel import ViewModel

class TestTodo:

    @staticmethod
    def test_trello_items_to_do():
    
        # Arrange
        items = get_trello_items()
        view_model = ViewModel(items, True)
    
        # Act
        to_do_items = view_model.to_do_items
    
        # Assert
        assert "To Do Card" == to_do_items[0].name
    
    @staticmethod
    def test_trello_items_doing():
    
        # Arrange
        items = get_trello_items()
        view_model = ViewModel(items, True)
    
        # Act
        doing_items = view_model.doing_items
    
        # Assert
        assert "Doing Card" == doing_items[0].name
    
    @staticmethod
    def test_trello_items_done():
    
        # Arrange
        items = get_trello_items()
        view_model = ViewModel(items, True)
    
        # Act
        done_items = view_model.done_items
    
        # Assert
        assert "Done Card" == done_items[0].name
    
    @staticmethod
    def test_trello_items_not_started():
    
        # Arrange
        items = get_trello_items()
        view_model = ViewModel(items, True)
    
        # Act
        not_started_items = view_model.not_started_items
    
        # Assert
        assert "Item 9" == not_started_items[0].name
        assert "Item 10" == not_started_items[1].name
        assert "Testing Update" == not_started_items[2].name
        assert "Test Can Still Add" == not_started_items[3].name
        assert "This is a test" == not_started_items[4].name
        assert "Item 1" == not_started_items[5].name
    
    @staticmethod
    def test_trello_items_in_progress():
    
        # Arrange
        items = get_trello_items()
        view_model = ViewModel(items, True)
    
        # Act
        in_progress_items = view_model.in_progress_items
    
        # Assert
        assert "Item 5" == in_progress_items[0].name
        assert "Item 7" == in_progress_items[1].name
    
    @staticmethod
    def test_trello_items_peer_review():
    
        # Arrange
        items = get_trello_items()
        view_model = ViewModel(items, True)
    
        # Act
        peer_review_items = view_model.peer_review_items
    
        # Assert
        assert "Item 4" == peer_review_items[0].name
        assert "Item 6" == peer_review_items[1].name
    
    @staticmethod
    def test_trello_items_on_hold():
    
        # Arrange
        items = get_trello_items()
        view_model = ViewModel(items, True)
    
        # Act
        on_hold_items = view_model.on_hold_items
    
        # Assert
        assert "Item 2" == on_hold_items[0].name
    
    @staticmethod
    def test_trello_items_completed():
    
        # Arrange
        items = get_trello_items()
        view_model = ViewModel(items, True)
    
        # Act
        completed_items = view_model.completed_items
    
        # Assert
        assert "Item 3" == completed_items[0].name

#not started
#in progress
#peer review
#on hold
#completed