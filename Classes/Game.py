#a class that handels an instance of a game
from Classes.Board import Board
import ast


class Game:
    def __init__(self,turn="w",isGameOver=False):
        self.game_board = Board()
        self.turn = turn
        self.isGameOver = isGameOver

    def execute_move(self):
        pass

    def start_game(self):
        while True:
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
                end_pos = ast.literal_eval(input(f"Enter end position : "))

            if self.turn == "b":
                self.turn = "w"
            else :
                self.turn = "b"
            

    def execute_move(self):
        pass
    