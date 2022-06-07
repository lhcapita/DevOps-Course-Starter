
import requests
import os
import pytest
from dotenv import load_dotenv, find_dotenv
import todo_app.app as app

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('../.env.test')
    load_dotenv(file_path, override=True)

    # Create the new app.
    test_app = app.create_app()

    with test_app.test_client() as client:
        yield client

class StubResponse():

    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data
    
    def json(self):
        return self.fake_response_data
    
def get_lists_stub(url, params, headers=None):
    test_board_id = os.environ.get('TRELLO_BOARD_ID')

    fake_response_data = None
    if url == f'https://api.trello.com/1/boards/{test_board_id}/lists/':
        fake_response_data = [{
            'id': '123abc',
            'name': 'To Do',
            'cards': [{'id': '456', 
                'name': 'Test card',
                'due': "2022-03-15T04:00:00.000Z",
                'desc': "testing"}]
        }]
    return StubResponse(fake_response_data)

def test_index_page(monkeypatch, client):
    # Replace call to requests.get(url) with our own function
    monkeypatch.setattr(requests, 'get', get_lists_stub)
    response = client.get('/')

    assert response.status_code == 200
    assert 'Test card' in response.data.decode()