from app.models.card import Card
from app.db import db
import pytest

def test_delete_card_by_id(client, one_card):
    response = client.delete('/cards/1')

    assert response.status_code == 204

    query = db.select(Card).where(Card.id == 1)
    
    assert db.session.scalar(query) is None

def test_delete_card_not_found(client, one_card):
    response = client.delete('/cards/5')

    assert response.status_code == 404
    assert response.get_json()['message'] == 'Card 5 not found'

def test_delete_card_invalid(client, one_card):
    response = client.delete('/cards/hey')

    assert response.status_code == 400
    assert response.get_json()['message'] == 'Card hey invalid'

def test_like_card_by_id(client, one_card):
    response = client.put('/cards/1/like')

    assert response.status_code == 204

    query = db.select(Card).where(Card.id == 1)
    card = db.session.scalar(query)

    assert card.likes_count == 1

def test_like_card_not_found(client, one_card):
    response = client.put('/cards/7/like')

    assert response.status_code == 404
    assert response.get_json()['message'] == 'Card 7 not found'

def test_like_card_invalid_id(client, one_card):
    response = client.put('/cards/seven/like')

    assert response.status_code == 400
    assert response.get_json()['message'] == 'Card seven invalid'