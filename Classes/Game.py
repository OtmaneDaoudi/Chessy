#a class that handels an instance of a game
from Classes.Board import Board
import ast
from enum import Enum

class GameStatus(Enum):
    ACTIVE = 1
    BLACK_WIN = 2
    WHITE_WIN = 3
    # BLACK_KING_CHECKED = 4
    # WHITE_KING_CHECKED = 5
    FORFIET = 4
    STALEMATE = 5
class Game:
    def __init__(self,turn="w",game_status = GameStatus.ACTIVE):
        self.game_board = Board()
        self.turn = turn
        self.game_status = game_status

    def execute_move(self):
        pass

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
                res = self.isCheck("w")
                if res == 0:
                    print("White king is under check")
                elif res == 1:    
                    print("Game is over , Black team wins")
                    self.game_status = GameStatus.BLACK_WIN
                self.turn = "w"
            else :
                res = self.isCheck("b")
                if res == 0:
                    print("Black king is under check")
                elif res == 1:
                    print("Game is Over, White team wins")
                    self.game_status = GameStatus.WHITE_WIN
                self.turn = "b"
        self.game_board.printBoard()


    #checks for king checks + checkmates
    def isCheck(self,color) -> int:
        #a player is in check mate when he is under check + he has no legal moves that will resolve the check
        #-1 ==> no check , 0 ==> color team is under check , 1 ==> color teams trapped under checkMate ==> other team wins
        #check if a given team's king is underCheck
        #loop over all other teams pieces and return if my king is in thier possible moves
        other_team_possible_moves = []
        for line in range(len(self.game_board.board)):
            for column in range(len(self.game_board.board[line])):
                if self.game_board.board[line][column] is not None and self.game_board.board[line][column].color != color:
                    other_team_possible_moves.extend(self.game_board.board[line][column].getPossibleMoves(self.game_board.board))

        if not ((color == "w" and self.game_board.white_king_position in other_team_possible_moves) or (color == "b" and self.game_board.black_king_position in other_team_possible_moves)):
            return -1
        
        #check if the player has no legal moves that will resolve the check 
        for line in range(len(self.game_board.board)):
            for column in range(len(self.game_board.board[line])):
                if self.game_board.board[line][column] is not None and self.game_board.board[line][column].color == color:
                    for move in self.game_board.board[line][column].getPossibleMoves(self.game_board.board):
                        if not self.game_board.MoveCauseCheck((line,column),move):
                            return 0
        return 1 

        
    def isStaleMate(self,color):
        pass


    