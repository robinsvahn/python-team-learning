from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

from Services.db_tutorial import Base


class Round(Base):
    __tablename__ = "Round"

    round_id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey("Game.game_id"))
    song_id = Column(Integer, ForeignKey("Song.song_id"))
