from msilib.schema import Error
from Services.db_service import Db_Service
from Model.game import Game
from Model.player import Player
from Model.song import Song
from Model.round import Round

import time
import os
import random


class Main:

    def __init__(self) -> None:
        self.db_service = Db_Service()
        self.current_game = None

        self.main_menu()

    def main_menu(self) -> None:
        self.clear_console()
        print(
            """Welcome to lyrically, do you want to load a saved game, or start a new one?
1 - Load a saved game
2 - Start a new game""")

        user_choice = self.get_user_choice_in_range("Your choice: ", 1, 2)
        self.navigate_to_option(user_choice)

        print()
        input("Press the enter key to go back to the main menu")
        self.current_game = None
        self.main_menu()

    def get_user_choice_in_range(self, text: str, lower: int, upper: int) -> int:
        response = input(text)
        while(not self.is_string_an_integer(response) or int(response) < lower or int(response) > upper):
            response = input(
                f"Input incorrect, please choose a number between {lower}-{upper}: ")
        return int(response)

    def is_string_an_integer(self, text: str) -> bool:
        try:
            text_as_int = int(text)
            return True
        except ValueError:
            return False

    def navigate_to_option(self, option: int) -> None:
        if(option == 1):
            self.start_menu_for_saved_games()
        elif(option == 2):
            self.start_new_game()
        else:
            print(
                "Hey dude, this is not supposed to happen, you should probably log this.")

    def start_menu_for_saved_games(self) -> None:
        saved_games = self.get_all_saved_games()
        self.clear_console()
        print("Here are all of the saved games: ")
        for game in saved_games:
            print(game)

        chosen_game_id = self.get_user_choice_in_range(
            "Enter a game ID to see the details of that game: ", 1, len(saved_games))
        self.current_game = saved_games[chosen_game_id - 1]
        print()
        print("Loading scoreboard...")
        time.sleep(2)
        self.clear_console()
        self.show_scoreboard()

    def get_all_saved_games(self) -> list:
        return self.db_service.get_saved_games()

    def start_new_game(self) -> None:
        print("Starting up a new game...")
        time.sleep(3)
        self.current_game = Game()
        self.clear_console()

        print("Lets play a game of lyrically!")
        player1 = Player(input("Player 1, please enter your name: "))
        player2 = Player(input("Player 2, please enter your name: "))
        print()

        self.current_game.players.append(player1)
        self.current_game.players.append(player2)

        self.show_scoreboard()

        self.start_new_round()

    def clear_console(self) -> None:
        os.system('cls')

    def show_scoreboard(self) -> None:
        print(f"Scoreboard - Round {len(self.current_game.rounds)}")
        print()
        for player in self.current_game.players:
            print(player)
        print()

    def start_new_round(self) -> None:
        print("Starting up a new round...")
        time.sleep(3)
        self.clear_console()

        new_round = Round(self.current_game.rounds)
        self.current_game.rounds.append(new_round)

        self.show_round(new_round)
        print("Round complete, loading scoreboard..")
        time.sleep(3)
        self.clear_console()
        self.show_scoreboard()

        if not self.is_game_finished():
            self.start_new_round()

    def show_round(self, this_round: Round) -> None:
        lyrics = self.db_service.get_lyrics_from_song_id(this_round.song_id)
        random.shuffle(lyrics)
        song = this_round.get_song()
        index = 1

        self.clear_console()
        print(f"In this round, the lyric in question is from the song:")
        print(f"{song.name} by {song.artist}")
        print()
        print(f"Which of the following lyrics is from that song: ")
        for lyric in lyrics:
            print(f"{index} - {lyric}")
            index += 1

        print()
        player1_guess = self.get_user_choice_in_range(
            f"{self.current_game.players[0].name} please enter your guess 1-4: ", 1, 4)
        player2_guess = self.get_user_choice_in_range(
            f"{self.current_game.players[1].name} please enter your guess 1-4: ", 1, 4)

        if lyrics[player1_guess-1].is_correct:
            self.current_game.players[0].score += 1
            print(f"{self.current_game.players[0].name} guessed correct!")
        if lyrics[player2_guess-1].is_correct:
            self.current_game.players[1].score += 1
            print(f"{self.current_game.players[1].name} guessed correct!")

    def is_game_finished(self) -> bool:
        if len(self.current_game.rounds) > 4:
            # To sort the list in place...
            self.current_game.players.sort(key=lambda x: x.score, reverse=True)
            print()
            if self.current_game.players[0].score == self.current_game.players[1].score:
                print("A tie! ")
            else:
                print(
                    f"Congratulations {self.current_game.players[0].name}, you won the match!")
            print("Thanks for playing!")
            self.db_service.save_game(self.current_game)
            return True
        else:
            return False


# Start game
Main()
