#a class that handels an instance of a game
from Classes.Board import Board


class Game:
    def __init__(self,turn="w",isGameOver=False):
        self.game_board = Board()
        self.turn = turn
        self.isGameOver = isGameOver

    def execute_move(self):
        pass

    