from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

from Services.db_tutorial import Base


class Song(Base):
    __tablename__ = "Song"

    song_id = Column(Integer, primary_key=True)
    rounds = relationship("Round", backref=backref("song"))
    lyrics = relationship("Lyric", backref=backref("song"))
    name = Column(String)
    artist = Column(String)
