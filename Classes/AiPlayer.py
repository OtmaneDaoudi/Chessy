from random import choice
from Classes.Board import Board
from Classes.King import King
from Classes.Pawn import Pawn
from Classes.Player import Player


class AiPlayer(Player):
    def __init__(self,color,difficulty):
        super().__init__(color)
        self.difficulty = difficulty

    #the implementation of the algorithm
    def getMove(self,game_board : Board) -> list:
        #create a data structure the maps every possible start position to its possible end possitions
        #exclude check positions
        res = {}
        for line in range(len(game_board.board)):
            for column in range(len(game_board.board[line])):
                if game_board.board[line][column] is not None and game_board.board[line][column].color == self.color:
                    possibleEndMoves = game_board.board[line][column].getPossibleMoves(game_board.board)
                    temp = []
                    for targetPos in possibleEndMoves:
                        if not game_board.MoveCauseCheck((line,column),targetPos):
                            temp.append(targetPos)
                    if len(temp) > 0 : #can move without check ==> create an entry
                        res[(line,column)] = temp

        #we're sure there will be at least one possible move , otherwise the game would have ended with a stalemate
        rand_key = choice(list(res.keys()))
        rand_value = choice(res[rand_key])
        # print(res)
        print(f"chess AI playing move : {rand_key} ==> {rand_value}")
        return (rand_key,rand_value)

