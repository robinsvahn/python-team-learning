from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

from Services.db_details import Base


class Lyric(Base):
    __tablename__ = "Lyric"

    lyric_id = Column(Integer, primary_key=True)
    song_id = Column(Integer, ForeignKey("Song.song_id"))
    text = Column(String)
    is_correct = Column(Boolean)

    def __init__(self, song_id, text, is_correct):
        self.song_id = song_id
        self.text = text
        self.is_correct = is_correct

    def __str__(self) -> str:
        return self.text
