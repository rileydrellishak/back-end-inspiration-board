from flask import Blueprint, request, Response
from app.models.card import Card
from ..db import db
from app.routes.route_utilities import create_model, delete_model, validate_model

bp = Blueprint('cards_bp', __name__, url_prefix='/cards')

# DELETE /cards/<card_id>
@bp.delete('/<card_id>')
def delete_card(card_id):
    return delete_model(Card, card_id)

#PUT /cards/<card_id>/like
@bp.put('/<card_id>/like')
def like_card(card_id):
    card = validate_model(Card, card_id)
    card.likes_count += 1
    db.session.commit()
    return Response(status=204, mimetype='application/json')