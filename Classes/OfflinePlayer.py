from Classes.Board import Board
from Classes.King import King
from Classes.Pawn import Pawn
from Classes.Player import Player
import ast

class OfflinePlayer(Player):
    def __init__(self,color):
        super().__init__(color)

    def getMove(self,game_board : Board) -> list:
        #get first selected square
        move = [None,None]
        while True:
            start_pos = ast.literal_eval(input(f"Enter start position : "))
            while game_board.board[start_pos[0]][start_pos[1]] is None or game_board.board[start_pos[0]][start_pos[1]].color != self.color:
                print("invalid selected piece , please try moving one of your pieces")
                start_pos = ast.literal_eval(input(f"Enter start position : "))
            move[0] = start_pos

            PossibleEndMoves = []
            PossibleEndMoves.extend(game_board.board[start_pos[0]][start_pos[1]].getPossibleMoves(game_board.board))
            if isinstance(game_board.board[start_pos[0]][start_pos[1]],Pawn):
                PossibleEndMoves.extend(game_board.board[start_pos[0]][start_pos[1]].getPossibleEnPassantCaptures(game_board.board).keys())
            if isinstance(game_board.board[start_pos[0]][start_pos[1]],King):
                PossibleEndMoves.extend(game_board.getPossibleCastleMoves(self.color))
            end_pos = ast.literal_eval(input(f"Enter end position : "))
            move[1] = end_pos
            if end_pos in PossibleEndMoves and not game_board.MoveCauseCheck(start_pos,end_pos): 
                break
            else : 
                print("illegal move")
        return move

