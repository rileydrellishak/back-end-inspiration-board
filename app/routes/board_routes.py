from flask import Blueprint, request, Response
from app.models.board import Board
from ..db import db
from app.routes.route_utilities import create_model, delete_model, validate_model

bp = Blueprint('boards_bp', __name__, url_prefix='/boards')

# GET /boards
@bp.get('')
def get_all_boards():
    pass

# POST /boards
@bp.post('')
def create_board():
    pass

# GET /boards/<board_id>/cards
@bp.get('/<board_id>/cards')
def get_cards_for_board_by_id(board_id):
    pass

# POST /boards/<board_id>/cards
@bp.post('/<board_id>/cards')
def post_card_to_board_by_id(board_id):
    pass