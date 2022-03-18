from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from Services.db_service import Db_Service
from Model.song import Song

import random

from Services.db_details import Base


class Round(Base):
    __tablename__ = "Round"

    round_id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey("Game.game_id"))
    song_id = Column(Integer, ForeignKey("Song.song_id"))

    def get_song(self) -> Song:
        return self.db_service.get_song_by_id(self.song_id)

    def __init__(self, existing_rounds: list) -> None:
        self.db_service = Db_Service()
        used_song_ids = []

        for round in existing_rounds:
            used_song_ids.append(round.song_id)
        self.song_id = self.get_random_unused_song(used_song_ids)

    def get_random_unused_song(self, used_song_ids: list) -> int:
        random_id = random.randint(1, 8)
        while random_id in used_song_ids:
            random_id = random.randint(1, 8)

        return random_id
