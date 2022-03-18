from Model.song import Song
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from Services.db_details import Base, engine, Session

from Model.song import Song
from Model.lyric import Lyric


class Db_Service:

    def __init__(self) -> None:
        # self.dialect = "mssql"
        # self.driver = "pyodbc"
        # self.host = "localhost\\SQLEXPRESS"
        # self.port = ""
        # self.database = "python_test"
        # self.trusted_connection = "trusted_connection=yes"
        # self.driver_specs = "driver=ODBC+Driver+17+for+SQL+Server"

        # self.engine = create_engine(
        #     f"{self.dialect}+{self.driver}://{self.host}/{self.database}?{self.trusted_connection}&{self.driver_specs}", echo=True)

        self.setup_session()

    def setup_session(self) -> None:
        self.session = Session()

    def get_song_by_id(self, song_id: int) -> Song:
        return self.session.query(Song).get(song_id)

    def get_lyrics_from_song_id(self, song_id: int) -> list:
        return self.session.query(Lyric).filter(
            Lyric.song_id == song_id).all()
