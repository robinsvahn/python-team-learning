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

# 3 - create a new session
session = Session()

lyrics_json = '''[
 {
   "song_id": 1,
   "text": "Fill up my cup, mazel tov Look at her dancin', just take it, off ",
   "is_correct": true
 },
 {
   "song_id": 1,
   "text": "Fill up my cup, mazel tov Look at her dancin', just shake it, off ",
   "is_correct": false
 },
 {
   "song_id": 1,
   "text": "Fill up my cup, buzz it up Look at her dancin', just take it, off ",
   "is_correct": false
 },
 {
   "song_id": 1,
   "text": "Fill up my cup, buzz it up Look at her dancin', just lit it, up",
   "is_correct": false
 },
 {
   "song_id": 2,
   "text": "Don't stop, make it pop, DJ blow my speakers up",
   "is_correct": true
 },
 {
   "song_id": 2,
   "text": "Don't stop, at the top, DJ, blow my speakers up",
   "is_correct": false
 },
 {
   "song_id": 2,
   "text": "Don't stop, make it drop, DJ blow my speakers up",
   "is_correct": false
 },
 {
   "song_id": 2,
   "text": "Don't stop, on the clock, DJ blow my speakers up ",
   "is_correct": false
 },
 {
   "song_id": 3,
   "text": "Can't read my, can't read my, no he can't read my poker face",
   "is_correct": true
 },
 {
   "song_id": 3,
   "text": "Carry me high, carry me high, though he can't read my poker face ",
   "is_correct": false
 },
 {
   "song_id": 3,
   "text": "Caring eye, caring eye, but he can't read my poker face ",
   "is_correct": false
 },
 {
   "song_id": 3,
   "text": "Can he lie, can he lie, when he can't read my poker face",
   "is_correct": false
 },
 {
   "song_id": 4,
   "text": "A few times I've been around that track ",
   "is_correct": true
 },
 {
   "song_id": 4,
   "text": "A few crimes I've seen around that track ",
   "is_correct": false
 },
 {
   "song_id": 4,
   "text": "A new kind I've seen around that track ",
   "is_correct": false
 },
 {
   "song_id": 4,
   "text": "A new rhyme I've heard around that track",
   "is_correct": false
 },
 {
   "song_id": 5,
   "text": "A foxtrot above my head, a sock hop beneath my bed",
   "is_correct": true
 },
 {
   "song_id": 5,
   "text": "A clock stopped from all that dread, a nonstop of dreams instead ",
   "is_correct": false
 },
 {
   "song_id": 5,
   "text": "A hot spot in what's unsaid, a long gone farewell to dread",
   "is_correct": false
 },
 {
   "song_id": 5,
   "text": "A lot of concern has spread, a pillow to rest my head  ",
   "is_correct": false
 },
 {
   "song_id": 6,
   "text": "Such a funny thing for me to try to explain, how I'm feeling, and my pride is the one to blame ",
   "is_correct": true
 },
 {
   "song_id": 6,
   "text": "Such an unlucky thing for me to entertain, how I'm feeling, and my pride is the one to blame ",
   "is_correct": false
 },
 {
   "song_id": 6,
   "text": "Such a stunning thing for me to try to embrace, how I'm feeling, and my pride won't be the same ",
   "is_correct": false
 },
 {
   "song_id": 6,
   "text": "Such a lovely thing for me to try to explain, how I'm feeling, and my pride won't be the same ",
   "is_correct": false
 },
 {
   "song_id": 7,
   "text": "You can find me in the club, bottle full of bub. ",
   "is_correct": true
 },
 {
   "song_id": 7,
   "text": "You're the kind of fancy club, with a bottle full of bub",
   "is_correct": false
 },
 {
   "song_id": 7,
   "text": "You can find me in the club, bottle full of bub. ",
   "is_correct": false
 },
 {
   "song_id": 7,
   "text": "You can grind me in the club, spillin' bottle full of bub",
   "is_correct": false
 },
 {
   "song_id": 8,
   "text": "I'll let you whip me if I misbehave, it's just that no one makes me feel this way",
   "is_correct": true
 },
 {
   "song_id": 8,
   "text": "I bet you'll trick me so I misbehave, it's just that no one makes you feel this way ",
   "is_correct": false
 },
 {
   "song_id": 8,
   "text": "I'll let you lick me if you misbehave, it's just that you can never be replaced ",
   "is_correct": false
 },
 {
   "song_id": 8,
   "text": "I felt you gripped me, did I misbehave? It's just that no one makes me feel this way ",
   "is_correct": false
 }
]'''

# Parse JSON into an object with attributes corresponding to dict keys.
items = json.loads(lyrics_json, object_hook=lambda d: SimpleNamespace(**d))

for x in items:
    # print(
    #     f"Song ID: {x.song_id} - Lyric Text: {x.text} - Is correct: {x.is_correct}")
    x_as_lyric = Lyric(x.song_id, x.text, x.is_correct)
    # x_as_song = Song(x.Song_Name, x.Artist)
    session.add(x_as_lyric)


# session.add(new_song)
# session.commit()
