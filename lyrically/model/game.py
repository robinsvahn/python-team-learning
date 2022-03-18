from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

from Services.db_details import Base


class Game(Base):
    __tablename__ = "Game"

    game_id = Column(Integer, primary_key=True)
    players = relationship("Player", backref=backref("Game"))
    rounds = relationship("Round", backref=backref("Game"))

    def __str__(self) -> str:
        return f"Game with the ID: {self.game_id}, it was played between {self.players[0].name} and {self.players[1].name}"
