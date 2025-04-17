import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Python Azure CI/CD demo!" in response.data

def test_add(client):
    response = client.get('/add?a=3&b=5')
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data['result'] == 8.0

def test_add_invalid_input(client):
    response = client.get('/add?a=hello&b=5')
    json_data = response.get_json()
    assert response.status_code == 400
    assert 'error' in json_data
