import pytest
from dotenv import load_dotenv, find_dotenv
import todo_app.app as app
from todo_app.data.db_items import DbHandler

import mongomock

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = app.create_app()
        with test_app.test_client() as client:
            yield client


def test_index_page(client):
    db = DbHandler()
    db.AddItem("Test Card", "Description", "12/12/2022")
    response = client.get('/')

    assert response.status_code == 200
    assert 'Test Card' in response.data.decode()