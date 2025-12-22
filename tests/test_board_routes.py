from app.models.board import Board
from app.db import db
import pytest

def test_boards_no_saved_boards(client):
    response = client.get('/boards')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_all_boards(client, three_boards):
    response = client.get('/boards')
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 3
    assert response_body == [
        {
            'id': 1,
            'title': 'Words of Wisdom ✨',
            'owner': 'Riley'
        },
        {
            'id': 2,
            'title': 'Happy Songs 🎵',
            'owner': 'Iris'
        },
        {
            'id': 3,
            'title': 'Encouragement 💪',
            'owner': 'Iris'
        }
    ]

def test_get_board_by_id(client, two_boards):
    response = client.get('/boards/1')
    response_body = response.get_json()
    assert response_body == {
        'id': 1,
        'title': 'Words of Wisdom ✨',
        'owner': 'Riley'
    }

def test_get_board_by_id_400_invalid(client, two_boards):
    response = client.get('/boards/one')
    response_body = response.get_json()
    assert response.status_code == 400
    assert response_body == {
        'message': 'Board one invalid'
    }

def test_get_board_by_id_404_not_found(client, two_boards):
    response = client.get('/boards/4')
    response_body = response.get_json()
    assert response.status_code == 404
    assert response_body == {
        'message': 'Board 4 not found'
    }

def test_create_board(client):
    response = client.post('/boards', json={
        "title": 'Morning Affirmations 🌄',
        'owner': 'Gina'
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == {
        'id': 1,
        'owner': 'Gina',
        'title': 'Morning Affirmations 🌄'
    }

    query = db.select(Board).where(Board.id == 1)
    new_board = db.session.scalar(query)

    assert new_board
    assert new_board.title == 'Morning Affirmations 🌄'
    assert new_board.owner == 'Gina'
    assert new_board.id == 1

def test_get_cards_for_board_by_id(client, board_with_cards):
    response = client.get('/boards/1/cards')
    response_body = response.get_json()

    assert response.status_code == 200
    assert type(response_body) == list
    assert len(response_body) == 3

    query = db.select(Board).where(Board.id == 1)
    board = db.session.scalar(query)

    assert len(board.cards) == 3
    for card in board.cards:
        assert card.board_id == 1
    
def test_post_card_to_board_by_id(client, one_board):
    response = client.post('/boards/1/cards', json={
        'title': 'Morning Affirmations 🌄',
        'owner': 'Gina'
    })
    response_body = response.get_json()
    
    assert response.status_code == 201

    # query card table to get card w id = 1 and board_id = 1
