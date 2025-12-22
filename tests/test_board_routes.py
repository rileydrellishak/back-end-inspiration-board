from app.models.board import Board
from app.db import db
import pytest

def test_boards_no_saved_boards(client):
    response = client.get('/boards')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []