from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

from Services.db_tutorial import Base


class Player(Base):
    __tablename__ = "Player"

    player_id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey("Game.game_id"))
    name = Column(String)
    score = Column(Integer)
