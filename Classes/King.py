from xmlrpc.client import Boolean
from Classes.Piece import Piece


class King(Piece):
    def __init__(self,rank,column,color,image = None) : 
        super().__init__(rank,column,color,image)

    def __str__(self):
        if  (self.color == "w"): return f"{Piece.WHITE_KING}"
        elif(self.color == "b"): return f"{Piece.BLACK_KING}"
        else :return ""

    def getPossibleMoves(self, board):
        res = []
        #the rule: king cannot capture other king will be implemented along the prohibition of check while moving pieces
        #up
        if self.rank + 1 <= 7 and self.checkSquare(self.rank + 1,self.column,board):
            res.append((self.rank + 1, self.column))
        #up right diagonal
        if self.rank + 1 <= 7 and self.column + 1 <= 7 and self.checkSquare(self.rank+1,self.column+1,board):
            res.append((self.rank+1, self.column+1))
        #right 
        if self.column + 1 <= 7 and self.checkSquare(self.rank,self.column + 1,board):
            res.append((self.rank,self.column + 1))
        
        #right down diagonal
        if self.rank - 1 >= 0 and self.column + 1 <= 7 and self.checkSquare(self.rank-1,self.column+1,board):
            res.append((self.rank-1,self.column+1))

        #down 
        if self.rank-1 >= 0 and self.checkSquare(self.rank-1, self.column, board):
            res.append((self.rank-1, self.column))
        
        #bottom left diagonal
        if self.rank-1 >= 0 and self.column-1 >= 0 and self.checkSquare(self.rank-1, self.column-1,board):
            res.append((self.rank-1, self.column-1))
        
        #left
        if self.column-1 >= 0 and self.checkSquare(self.rank, self.column-1, board):
            res.append((self.rank, self.column-1))

        #up left diagonal
        if self.rank+1 <= 7 and self.column-1 >= 0 and self.checkSquare(self.rank+1, self.column-1, board):
            res.append((self.rank+1, self.column-1))
            
        return res

    def checkSquare(self, rank, column, board) -> Boolean:
        return (board[rank][column] is None or (board[rank][column].color != self.color))# and not isinstance(board[rank][column],King)))
        