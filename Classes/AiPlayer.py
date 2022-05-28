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
import UI.gameUI as gameUi


class AiPlayer(Player):
    Thread_exit_state = False
    #negative values for black , positive for white
    PAWN = 100
    KNIGHT = 280
    BISHOP = 320
    ROOK = 479
    QUEEN = 929
    KING = 60000

    pst = {
    'P': [[ 0,   0,   0,   0,   0,   0,   0,   0],
           [ 78,  83,  86,  73, 102,  82,  85,  90],
           [  7,  29,  21,  44,  40,  31,  44,   7],
           [-17,  16,  -2,  15,  14,   0,  15, -13],
           [-26,   3,  10,   9,   6,   1,   0, -23],
           [-22,   9,   5, -11, -10,  -2,   3, -19],
           [-31,   8,  -7, -37, -36, -14,   3, -31],
            [0,   0,   0,   0,   0,   0,   0,   0]]

    ,'N': [[-66, -53, -75, -75, -10, -55, -58, -70 ],
          [  -3,  -6, 100, -36,   4,  62,  -4, -14],
          [  10,  67,   1,  74,  73,  27,  62,  -2],
          [  24,  24,  45,  37,  33,  41,  25,  17],
          [  -1,   5,  31,  21,  22,  35,   2,   0],
          [ -18,  10,  13,  22,  18,  15,  11, -14],
          [ -23, -15,   2,   0,   2,   0, -23, -20],
          [ -74, -23, -26, -24, -19, -35, -22, -69]]
    ,'B': [[-59, -78, -82, -76, -23,-107, -37, -50],
           [-11,  20,  35, -42, -39,  31,   2, -22],
           [ -9,  39, -32,  41,  52, -10,  28, -14],
           [ 25,  17,  20,  34,  26,  25,  15,  10],
           [ 13,  10,  17,  23,  17,  16,   0,   7],
           [ 14,  25,  24,  15,   8,  25,  20,  15],
           [ 19,  20,  11,   6,   7,   6,  20,  16],
           [ -7,   2, -15, -12, -14, -15, -10, -10]]
    ,'R': [  [35,  29,  33,   4,  37,  33,  56,  50 ],
             [55,  29,  56,  67,  55,  62,  34,  60 ],
             [19,  35,  28,  33,  45,  27,  25,  15  ],
             [0,   5,  16,  13,  18,  -4,  -9,  -6  ],
             [-28, -35, -16, -21, -13, -29, -46, -30 ],
             [-42, -28, -42, -25, -25, -35, -26, -46 ],
             [-53, -38, -31, -26, -29, -43, -44, -53 ],
             [-30, -24, -18,   5,  -2, -18, -31, -32]]
    ,'Q': [[  6,   1,  -8,-104,  69,  24,  88,  26],
            [  14,  32,  60, -10,  20,  76,  57,  24],
            [  -2,  43,  32,  60,  72,  63,  43,   2],
            [  1, -16,  22,  17,  25,  20, -13,  -6],
            [  -14, -15,  -2,  -5,  -1, -10, -20, -22],
            [  -30,  -6, -13, -11, -16, -11, -16, -27],
            [ -36, -18,   0, -19, -15, -15, -21, -38],
            [ -39, -30, -31, -13, -31, -36, -34, -42]]
    ,'K': [  [ 4,  54,  47, -99, -99,  60,  83, -62],
              [-32,  10,  55,  56,  56,  55,  10,   3],
              [-62,  12, -57,  44, -67,  28,  37, -31],
              [-55,  50,  11,  -4, -19,  13,   0, -49],
              [-55, -43, -52, -28, -51, -47,  -8, -50],
              [-47, -42, -43, -79, -64, -32, -29, -32],
              [-4,   3, -14, -50, -57, -18,  13,   4],
              [ 17,  30,  -3, -14,   6,  -1,  40,  18]],
    }



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
        if depth == 0 or position.isGameOver() or gameUi.ChessBoard.thread_flag == "ENDED":
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
                        res += factor*(AiPlayer.PAWN + AiPlayer.pst['P'][line][column])
                    elif isinstance(position.board[line][column],Bishop):
                        res += factor*(AiPlayer.BISHOP + AiPlayer.pst['B'][line][column])
                    elif isinstance(position.board[line][column],Rook):
                        res += factor*(AiPlayer.ROOK + AiPlayer.pst['R'][line][column])
                    elif isinstance(position.board[line][column],Knight):
                        res += factor*(AiPlayer.KNIGHT + AiPlayer.pst['N'][line][column])
                    elif isinstance(position.board[line][column],Queen):
                        res += factor*(AiPlayer.QUEEN + AiPlayer.pst['Q'][line][column])
                    elif isinstance(position.board[line][column],King):
                        res += factor*(AiPlayer.KING + AiPlayer.pst['K'][line][column])
        return res

    def getAllMoves(self,position: Board,color):
        res = {}
        #random indexes shuflling allows for random best move selection
        lines = list(range(8))
        shuffle(lines)
        columns = list(range(8))
        shuffle(columns)
        # lines = range(8)
        # columns = range(8)
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