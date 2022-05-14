#a class that handels an instance of a game
from Classes.AiPlayer import AiPlayer
from Classes.Board import Board
import ast
from enum import Enum
from Classes.OfflinePlayer import OfflinePlayer

from Classes.Player import Player
import UI.gameUI as chessUI

class GameStatus(Enum):
    ACTIVE = 1
    BLACK_WIN = 2
    WHITE_WIN = 3
    FORFIET = 4
    STALEMATE = 5
    INSUFFICIENT_MATERIAL = 6
class Game:
    def __init__(self,boardUI: chessUI,turn="w"):
        self.game_board = Board()
        self.turn = turn
        self.game_status = GameStatus.ACTIVE
        

    def start_game(self):
        white_player = AiPlayer("w",2)
        black_player = OfflinePlayer("b")

        #initialise Game UI
        
        while self.game_status == GameStatus.ACTIVE:
            #eval a tuple from user input
            self.game_board.printBoard()
            turn_var = "white" if self.turn == "w" else "black"
            print(f"{turn_var}'s turn")

            if self.game_board.isStaleMate("b") or self.game_board.isStaleMate("w"):
                        print("Game is over, Stalemate")
                        self.game_status = GameStatus.STALEMATE 
            elif self.game_board.isInsufficientMaterial():
                        print("Game is Over, Draw by insufficient material")
                        self.game_status = GameStatus.INSUFFICIENT_MATERIAL
            elif self.turn == "b":
                move = black_player.getMove(self.game_board) #returns a valid move
                black_AI_autopromotion = (True if isinstance(black_player,AiPlayer) else False)
                print(f"move stat : {self.game_board.move_piece(move[0],move[1],black_AI_autopromotion)}")
                if self.game_board.isCheck("w") :
                    if self.game_board.isCheckMate("w"):
                        print("Game is over, black team wins")
                        self.game_status = GameStatus.BLACK_WIN
                    else :
                        print("White king is under check")
                self.turn = "w"

            else:
                move = white_player.getMove(self.game_board) #returns a valid move
                white_AI_autopromotion = (True if isinstance(white_player,AiPlayer) else False)
                print(f"move stat : {self.game_board.move_piece(move[0],move[1],white_AI_autopromotion)}")
                if self.game_board.isCheck("b") :
                    if self.game_board.isCheckMate("b"):
                        print("Game is over, white team wins")
                        self.game_status = GameStatus.WHITE_WIN
                    else :
                        print("black king is under check")
                self.turn = "b"

        self.game_board.printBoard()

    def switchTurnes(self):
        self.turn = "b" if self.turn == "w" else "w"

    def selected(self,):
        pass