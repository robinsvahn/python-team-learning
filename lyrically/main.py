from Model.game import Game
from Services.db_service import Db_Service


class Main:

    def __init__(self) -> None:
        self.db_service = Db_Service()
        self.db_service.setup_db_connection()


# Start game
Main()
