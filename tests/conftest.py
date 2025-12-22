import pytest
from app import create_app
from app.db import db
from flask.signals import request_finished
from dotenv import load_dotenv
import os
from app.models.board import Board
from app.models.card import Card

load_dotenv()

@pytest.fixture
def app():
    # create the app with a test configuration
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    }
    app = create_app(test_config)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    # close and remove the temporary database
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


# This fixture gets called in every test that
# references "one_card"
# This fixture creates a card and saves it in the database
@pytest.fixture
def one_card(app):
    board_1 = Board(
        title='Encouragement 💪',
        owner='Iris'
    )
    new_card = Card(
        message='You rock! 🤘',
        board_id=1,
        likes_count=0
        )
    db.session.add_all([board_1, new_card])
    db.session.commit()

@pytest.fixture
def two_cards(app):
    card_1 = Card(
        message='You rock! 🤘',
        likes_count=0
    )
    card_2 = Card(
        message='Here comes the sun ☀️',
        likes_count=0
    )
    db.session.add_all([card_1, card_2])
    db.session.commit()

@pytest.fixture
def three_cards(app):
    card_1 = Card(
        message='You rock! 🤘',
        likes_count=0
    )
    card_2 = Card(
        message='Here comes the sun ☀️',
        likes_count=0
    )
    card_3 = Card(
        message='Like if you like snow ❄️',
        likes_count=0
    )
    db.session.add_all([card_1, card_2, card_3])
    db.session.commit()

@pytest.fixture
def one_board(app):
    board_1 = Board(
        title='Words of Wisdom ✨',
        owner='Riley'
    )
    db.session.add(board_1)
    db.session.commit()

@pytest.fixture
def two_boards(app):
    board_1 = Board(
        title='Words of Wisdom ✨',
        owner='Riley'
    )
    board_2 = Board(
        title='Happy Songs 🎵',
        owner='Iris'
    )
    db.session.add_all([board_1, board_2])
    db.session.commit()

@pytest.fixture
def three_boards(app):
    board_1 = Board(
        title='Words of Wisdom ✨',
        owner='Riley'
    )
    board_2 = Board(
        title='Happy Songs 🎵',
        owner='Iris'
    )
    board_3 = Board(
        title='Encouragement 💪',
        owner='Iris'
    )
    db.session.add_all([board_1, board_2, board_3])
    db.session.commit()

@pytest.fixture
def board_with_cards(app):
    board_1 = Board(
        title='Words of Wisdom ✨',
        owner='Riley'
    )
    db.session.add(board_1)
    card_1 = Card(
        message='You rock! 🤘',
        likes_count=0,
        board_id=1
    )
    card_2 = Card(
        message='Think positively ✨',
        likes_count=0,
        board_id=1
    )
    card_3 = Card(
        message='Follow your curiosity 🤔',
        likes_count=0,
        board_id=1
    )
    db.session.add_all([card_1, card_2, card_3])
    db.session.commit()