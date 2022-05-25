from chess import Board
from Classes.Game import GameStatus

class serialisedGame:
    def __init__(self, game_board:Board, turn: str, game_status: GameStatus, gameMode, white_timer, black_timer, playas, diff = 1):
        self.game_board = game_board
        self.turn = turn
        self.game_status = game_status
        self.gameMode = gameMode
        self.white_timer = white_timer
        self.black_timer = black_timer
        self.playas = playas
        self.diff = diff