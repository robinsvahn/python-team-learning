from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from Services.db_details import Base, engine, Session

from Model.song import Song
from Model.lyric import Lyric
from Model.game import Game


class Db_Service:

    def __init__(self) -> None:
        self.setup_session()

    def setup_session(self) -> None:
        self.session = Session()

    def get_song_by_id(self, song_id: int) -> Song:
        return self.session.query(Song).get(song_id)

    def get_lyrics_from_song_id(self, song_id: int) -> list:
        return self.session.query(Lyric).filter(
            Lyric.song_id == song_id).all()

    def save_game(self, game: Game) -> None:
        self.session.add(game)
        self.session.commit()

    def get_saved_games(self) -> list:
        return self.session.query(Game).all()
