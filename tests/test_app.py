import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_create_task(client):
    response = client.post('/tasks', json={"title": "Estudar CI"})
    assert response.status_code == 201

def test_get_tasks(client):
    response = client.get('/tasks')
    assert response.status_code == 200

def test_complete_task(client):
    client.post('/tasks', json={"title": "Teste"})
    response = client.put('/tasks/1')
    assert response.status_code == 200