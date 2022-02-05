class Player:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self) -> str:
        return f"The player {self.name} playing the position {self.position}"
