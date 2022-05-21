from copy import deepcopy
import math
from random import shuffle
from Classes.Bishop import Bishop
from Classes.Board import Board
from Classes.King import King
from Classes.Knight import Knight
from Classes.Pawn import Pawn
from Classes.Player import Player
from Classes.Queen import Queen
from Classes.Rook import Rook


class AiPlayer(Player):
    Thread_exit_state = False
    #negative values for black , positive for white
    PAWN = 10
    KNIGHT = 30
    BISHOP = 30
    ROOK = 50
    QUEEN = 90
    KING = 900

    def __init__(self,color,difficulty):
        super().__init__(color)
        self.difficulty = difficulty
    
    def getMove(self,game_board : Board) -> list:
        maximizing = (False if self.color == "b" else True)
        res = self.minimax(game_board, self.difficulty, -math.inf, math.inf, maximizing)[1]
        print(f"chess AI playin move : {res[0]}==>{res[1]}")
        return res

    #white ==> maximising player
    #black ==> minimising player

    #beta ==> worst possbile score for black
    #alpha==> worst possible score for white

    # def minimax(self,position: Board, depth: int, maximizingPlayer: bool):
    #     #if the game ends at the current position or depth == 0
    #     if depth == 0 or self.isGameOver(position):
    #         return self.evaluatePosition(position), None

    #     if maximizingPlayer:
    #         possibleMoves = self.getAllMoves(position, "w")
    #         maxEval = -math.inf
    #         best_move = None
    #         for start in possibleMoves.keys():
    #             for end in possibleMoves[start]:
    #                 board_copy = deepcopy(position)
    #                 position.AiAutoPromotion = True
    #                 board_copy.move_piece(start, end)
    #                 eval = self.minimax(board_copy, depth - 1, False)[0]
    #                 maxEval = max(maxEval, eval)
    #                 if maxEval == eval:
    #                     best_move = [start,end]
    #         return maxEval, best_move

    #     else:
    #         possibleMoves = self.getAllMoves(position, "b")
    #         print(possibleMoves)
    #         print(possibleMoves)
    #         minEval = math.inf
    #         best_move = None
    #         for start in possibleMoves.keys():
    #             for end in possibleMoves[start]:
    #                 board_copy = deepcopy(position)
    #                 position.AiAutoPromotion = True
    #                 board_copy.move_piece(start, end)
    #                 eval = self.minimax(board_copy, depth - 1, True)[0]
    #                 minEval = min(minEval, eval)
    #                 if minEval == eval:
    #                     best_move = [start,end]
    #         return minEval, best_move
            
    def minimax(self, position: Board, depth: int,alpha, beta, maximizingPlayer: bool):
        #if the game ends at the current position or depth == 0
        if depth == 0 or position.isGameOver():
            return self.evaluatePosition(position), None

        if maximizingPlayer:
            possibleMoves = self.getAllMoves(position, "w")
            maxEval = -math.inf
            best_move = None
            for start in possibleMoves.keys():
                for end in possibleMoves[start]:
                    board_copy = deepcopy(position)
                    board_copy.move_piece(start, end, None, True)
                    eval = self.minimax(board_copy, depth - 1,alpha,beta, False)[0]
                    maxEval = max(maxEval, eval)
                    alpha = max(alpha, eval)
                    if maxEval == eval:
                        best_move = [start,end]
                    if beta <= alpha:
                        break
            return maxEval, best_move
        else:
            possibleMoves = self.getAllMoves(position, "b")
            minEval = math.inf
            best_move = None
            for start in possibleMoves.keys():
                for end in possibleMoves[start]:
                    board_copy = deepcopy(position)
                    board_copy.move_piece(start, end,None, True)
                    eval = self.minimax(board_copy, depth - 1,alpha,beta, True)[0]
                    minEval = min(minEval, eval)
                    beta = min(beta, eval)
                    if minEval == eval:
                        best_move = [start,end]
                    if beta <= alpha:
                        break    
            return minEval, best_move

    #static evaluation of a po sition
    def evaluatePosition(self,position : Board):
        res = 0
        for line in range(8):
            for column in range(8):
                if position.board[line][column] is not None:
                    factor = (1 if position.board[line][column].color == "w" else -1)
                    if isinstance(position.board[line][column],Pawn):
                        res += factor*AiPlayer.PAWN
                    elif isinstance(position.board[line][column],Bishop):
                        res += factor*AiPlayer.BISHOP
                    elif isinstance(position.board[line][column],Rook):
                        res += factor*AiPlayer.ROOK
                    elif isinstance(position.board[line][column],Knight):
                        res += factor*AiPlayer.KNIGHT
                    elif isinstance(position.board[line][column],Queen):
                        res += factor*AiPlayer.QUEEN
                    elif isinstance(position.board[line][column],King):
                        res += factor*AiPlayer.KING
        return res

    def getAllMoves(self,position: Board,color):
        res = {}
        #random indexes shuflling allows for random best move selection
        lines = list(range(8))
        shuffle(lines)
        columns = list(range(8))
        shuffle(columns)
        for line in lines:
            for column in columns:
                if position.board[line][column] is not None and position.board[line][column].color == color:
                    possibleEndMoves = position.board[line][column].getPossibleMoves(position.board)
                    if isinstance(position.board[line][column],Pawn):
                        possibleEndMoves.extend(list(position.board[line][column].getPossibleEnPassantCaptures(position.board).keys()))
                    if isinstance(position.board[line][column],King):
                        possibleEndMoves.extend(position.getPossibleCastleMoves(position.board[line][column].color))
                    temp = []
                    for targetPos in possibleEndMoves:
                        if not position.MoveCauseCheck((line,column),targetPos):
                            temp.append(targetPos)
                    if len(temp) > 0 : #can move without check ==> create an entry
                        res[(line,column)] = temp
        return res