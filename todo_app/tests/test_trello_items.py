from todo_app.data.trello_items import get_trello_items, get_trello_lists
from todo_app.data.IndexViewModel import ViewModel
from dotenv import load_dotenv, find_dotenv
import todo_app.app as app

class TestTodo:

    @staticmethod
    def test_trello_items_to_do():
    
        # Arrange    
        file_path = find_dotenv('../.env')
        load_dotenv(file_path, override=True)

        test_app = app.create_app()
        items = get_trello_items()
        trello_lists = get_trello_lists()
        view_model = ViewModel(items, trello_lists, True)
    
        # Act
        to_do_items = view_model.to_do_items
    
        # Assert
        assert "To Do Card" == to_do_items[0].name
    
    @staticmethod
    def test_trello_items_doing():
    
        # Arrange
        file_path = find_dotenv('../.env')
        load_dotenv(file_path, override=True)

        test_app = app.create_app()
        items = get_trello_items()
        trello_lists = get_trello_lists()
        view_model = ViewModel(items, trello_lists, True)
    
        # Act
        doing_items = view_model.doing_items
    
        # Assert
        assert "Doing Card" == doing_items[0].name
    
    @staticmethod
    def test_trello_items_done():
    
        # Arrange
        file_path = find_dotenv('../.env')
        load_dotenv(file_path, override=True)

        test_app = app.create_app()
        items = get_trello_items()
        trello_lists = get_trello_lists()
        view_model = ViewModel(items, trello_lists, True)
    
        # Act
        done_items = view_model.done_items
    
        # Assert
        assert "Done Card" == done_items[0].name
    
    @staticmethod
    def test_trello_items_not_started():
    
        # Arrange
        file_path = find_dotenv('../.env')
        load_dotenv(file_path, override=True)

        test_app = app.create_app()
        items = get_trello_items()
        trello_lists = get_trello_lists()
        view_model = ViewModel(items, trello_lists, True)
    
        # Act
        not_started_items = view_model.not_started_items
    
        # Assert
        assert "Item 1" == not_started_items[0].name
        assert "Item 9" == not_started_items[1].name
        assert "Item 10" == not_started_items[2].name
    
    @staticmethod
    def test_trello_items_in_progress():
    
        # Arrange
        file_path = find_dotenv('../.env')
        load_dotenv(file_path, override=True)

        test_app = app.create_app()
        items = get_trello_items()
        trello_lists = get_trello_lists()
        view_model = ViewModel(items, trello_lists, True)
    
        # Act
        in_progress_items = view_model.in_progress_items
    
        # Assert
        assert "Item 5" == in_progress_items[0].name
        assert "Item 7" == in_progress_items[1].name
    
    @staticmethod
    def test_trello_items_peer_review():
    
        # Arrange
        file_path = find_dotenv('../.env')
        load_dotenv(file_path, override=True)

        test_app = app.create_app()
        items = get_trello_items()
        trello_lists = get_trello_lists()
        view_model = ViewModel(items, trello_lists, True)
    
        # Act
        peer_review_items = view_model.peer_review_items
    
        # Assert
        assert "Item 4" == peer_review_items[0].name
        assert "Item 6" == peer_review_items[1].name
    
    @staticmethod
    def test_trello_items_on_hold():
    
        # Arrange
        file_path = find_dotenv('../.env')
        load_dotenv(file_path, override=True)

        test_app = app.create_app()
        items = get_trello_items()
        trello_lists = get_trello_lists()
        view_model = ViewModel(items, trello_lists, True)
    
        # Act
        on_hold_items = view_model.on_hold_items
    
        # Assert
        assert "Item 2" == on_hold_items[0].name
    
    @staticmethod
    def test_trello_items_completed():
    
        # Arrange
        file_path = find_dotenv('../.env')
        load_dotenv(file_path, override=True)

        test_app = app.create_app()
        items = get_trello_items()
        trello_lists = get_trello_lists()
        view_model = ViewModel(items, trello_lists, True)
    
        # Act
        completed_items = view_model.completed_items
    
        # Assert
        assert "Item 3" == completed_items[0].name
    
    @staticmethod
    def test_trello_items_sorted():
    
        # Arrange
        file_path = find_dotenv('../.env')
        load_dotenv(file_path, override=True)

        test_app = app.create_app()
        items = get_trello_items()
        trello_lists = get_trello_lists()
        view_model = ViewModel(items, trello_lists, True)
    
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
        assert "To Do Card" == sorted_items["To Do"][0].name
        assert "Doing Card" == sorted_items["Doing"][0].name
        assert "Done Card" == sorted_items["Done"][0].name
