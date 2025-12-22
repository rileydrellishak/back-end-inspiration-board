from flask import Blueprint, request, Response
from app.models.board import Board
from app.models.card import Card
from ..db import db
from app.routes.route_utilities import create_model, delete_model, get_models_with_filters, update_model, validate_model

bp = Blueprint('boards_bp', __name__, url_prefix='/boards')

# GET /boards
@bp.get('')
def get_all_boards():
    filters = request.args
    return get_models_with_filters(Board, filters)

# POST /boards
@bp.post('')
def create_board():
    request_body = request.get_json()
    new_board = create_model(Board, request_body)
    return new_board.to_dict(), 201

# GET /boards/<board_id>/cards
@bp.get('/<board_id>/cards')
def get_cards_for_board_by_id(board_id):
    board = validate_model(Board, board_id)
    response = [card.to_dict() for card in board.cards]
    return response, 200


# POST /boards/<board_id>/cards
@bp.post('/<board_id>/cards')
def post_card_to_board_by_id(board_id):
    board = validate_model(Board, board_id)
    request_body = request.get_json()
    new_card = create_model(Card, request_body)
    new_card['board_id'] = board.id
    new_card['board'] = board.title
    return new_card, 201