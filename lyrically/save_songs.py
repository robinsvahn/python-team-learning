# 1 - imports
from datetime import date

from Model.game import Game
from Model.lyric import Lyric
from Model.player import Player
from Model.round import Round
from Model.song import Song
from Services.db_details import Base, Session, engine
import pyodbc

import json
from types import SimpleNamespace

# 2 - generate database schema


# 3 - create a new session
session = Session()

new_song = Song("I Gotta Feeling", "Black Eyed Peas")

json_songs = '''[
 {
   "Song_Name": "TiK ToK",
   "Artist": "Kesha"
 },
 {
   "Song_Name": "Poker Face",
   "Artist": "Lady Gaga"
 },
 {
   "Song_Name": "Hollaback Girl",
   "Artist": "Gwen Stefani"
 },
 {
   "Song_Name": "Fireflies",
   "Artist": "Owl City "
 },
 {
   "Song_Name": "Crazy In Love",
   "Artist": "Beyoncé"
 },
 {
   "Song_Name": "In Da Club",
   "Artist": "50 Cent"
 },
 {
   "Song_Name": "Sexy Back ",
   "Artist": "Justin Timberlake"
 },
 {
   "Song_Name": "Don't Stop The Music",
   "Artist": "Rihanna"
 },
 {
   "Song_Name": "Firework",
   "Artist": "Katy Perry "
 },
 {
   "Song_Name": "Dynamite",
   "Artist": "Taio Cruz"
 },
 {
   "Song_Name": "Cry Me A River",
   "Artist": "Justin Timberlake"
 },
 {
   "Song_Name": "You're Beautiful",
   "Artist": "James Blunt"
 },
 {
   "Song_Name": "Oops!...I Did It Again",
   "Artist": "Britney Spears"
 },
 {
   "Song_Name": "Survivor",
   "Artist": "Destiny's Child"
 },
 {
   "Song_Name": "Beautiful ",
   "Artist": "Christina Aguilera"
 },
 {
   "Song_Name": "Party In The U.S.A",
   "Artist": "Miley Cyrus"
 },
 {
   "Song_Name": "What Makes You Beautiful",
   "Artist": "One Direction"
 },
 {
   "Song_Name": "Hips Don't Lie",
   "Artist": "Shakira feat. Wyclef Jean "
 },
 {
   "Song_Name": "So Sick ",
   "Artist": "Ne-Yo"
 },
 {
   "Song_Name": "Africa",
   "Artist": "TOTO"
 },
 {
   "Song_Name": "I Wanna Dance With Somebody",
   "Artist": "Whitney Houston"
 },
 {
   "Song_Name": "Hotel California",
   "Artist": "Eagles"
 },
 {
   "Song_Name": "Never Gonna Give You Up",
   "Artist": "Rick Astley"
 },
 {
   "Song_Name": "Like a Prayer",
   "Artist": "Madonna"
 }
]'''

# Parse JSON into an object with attributes corresponding to dict keys.
items = json.loads(json_songs, object_hook=lambda d: SimpleNamespace(**d))

for x in items:
    x_as_song = Song(x.Song_Name, x.Artist)
    session.add(x_as_song)


# session.add(new_song)
# session.commit()
