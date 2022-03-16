# 1 - imports
from datetime import date

from Model.game import Game
from Model.lyric import Lyric
from Model.player import Player
from Model.round import Round
from Model.song import Song
from Services.db_tutorial import Base, Session, engine
import pyodbc

print(pyodbc.drivers())

# 2 - generate database schema
Base.metadata.create_all(engine)


# 3 - create a new session
session = Session()
