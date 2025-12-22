from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from sqlalchemy import ForeignKey
from typing import Optional

class Card(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    message: Mapped[str]
    likes_count: Mapped[Optional[int]]
    board_id: Mapped[int]=mapped_column(ForeignKey("board.id"))
    board: Mapped[Optional["Board"]] = relationship(back_populates="cards")

    def to_dict(self):
        result = {
            "id": self.id,
            "message": self.message,
            "likes_count": self.likes_count if self.likes_count else 0,
        }
        return result

# Card request body
# {
#     "message": ...,
#     "likes_count": ...,
#     "board_id": ...
# }