#a class that handels an instance of a game
from Classes.Board import Board
import ast
from enum import Enum

class GameStatus(Enum):
    ACTIVE = 1
    BLACK_WIN = 2
    WHITE_WIN = 3
    FORFIET = 4
    STALEMATE = 5
class Game:
    def __init__(self,turn="w"):
        self.game_board = Board()
        self.turn = turn
        self.game_status = GameStatus.ACTIVE

    def start_game(self):
        while self.game_status == GameStatus.ACTIVE:
            #eval a tuple from user input
            self.game_board.printBoard()
            turn_var = "white" if self.turn == "w" else "black"
            print(f"{turn_var}'s turn")
            start_pos = ast.literal_eval(input(f"Enter start position : "))

            while self.game_board.board[start_pos[0]][start_pos[1]] is None or self.game_board.board[start_pos[0]][start_pos[1]].color != self.turn:
                print("invalid selected piece , please try moving one of your pieces")
                start_pos = ast.literal_eval(input(f"Enter start position : "))
                
            end_pos = ast.literal_eval(input(f"Enter end position : "))
            while not self.game_board.move_piece(start_pos,end_pos): #unsuccessfull move
                print("illegal move")
                start_pos = ast.literal_eval(input(f"Enter start position : "))
                end_pos = ast.literal_eval(input(f"Enter end position : "))
            
            if self.turn == "b":
                if self.game_board.isCheck("w") :
                    if self.game_board.isCheckMate("w"):
                        print("Game is over, black team wins")
                        self.game_status = GameStatus.BLACK_WIN
                    else :
                        print("White king is under check")
                else:
                    if self.game_board.isStaleMate("w"):
                        print("Game is over, Stalemate")
                        self.game_status = GameStatus.STALEMATE
                self.turn = "w"

            else :
                if self.game_board.isCheck("b") :
                    if self.game_board.isCheckMate("b"):
                        print("Game is over, white team wins")
                        self.game_status = GameStatus.BLACK_WIN
                    else :
                        print("black king is under check")
                else :
                    if self.game_board.isStaleMate("b"):
                        print("Game is over, Stalemate")
                        self.game_status = GameStatus.STALEMATE
                self.turn = "b"

        self.game_board.printBoard()