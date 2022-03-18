from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

from Services.db_details import Base


class Player(Base):
    __tablename__ = "Player"

    player_id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey("Game.game_id"))
    name = Column(String)
    score = Column(Integer)

    def __init__(self, name: str) -> None:
        super().__init__()

        self.name = name
        self.score = 0

    
    def __str__(self) -> str:
        return f"Player: {self.name}, Score: {self.score}"
