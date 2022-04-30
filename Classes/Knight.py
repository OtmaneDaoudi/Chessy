from Classes.Piece import Piece


class Knight(Piece):
    def __init__(self,rank,column,color,image = None) : 
        super().__init__(rank,column,color,image)

    def __str__(self):
        if  (self.color == "w"): return f"{Piece.WHITE_KNIGHT}"
        elif(self.color == "b"): return f"{Piece.BLACK_KNIGHT}"
        else :return ""

    def getPossibleMoves(self,board):
        res = []
        #up
        if self.rank + 2 <= 7:
            if self.column + 1 <= 7 and (board[self.rank + 2][self.column + 1] is None or board[self.rank + 2][self.column + 1].color != self.color):
                res.append((self.rank + 2, self.column + 1))
            if self.column - 1 >= 0 and (board[self.rank + 2][self.column - 1] is None or board[self.rank + 2][self.column - 1].color != self.color):
                res.append((self.rank + 2, self.column - 1))

        #right
        if self.column + 2 <= 7:
            if self.rank + 1 <= 7 and (board[self.rank + 1][self.column + 2] is None or board[self.rank + 1][self.column + 2].color != self.color):
                res.append((self.rank + 1,self.column + 2))
            if self.rank - 1 >= 0 and (board[self.rank - 1][self.column + 2] is None or board[self.rank - 1][self.column + 2].color != self.color):
                res.append((self.rank - 1, self.column + 2))

        #left
        if self.column - 2 >= 0:
            if self.rank + 1 <= 7 and (board[self.rank + 1][self.column -2] is None or board[self.rank + 1][self.column -2].color != self.color):
                res.append((self.rank + 1, self.column - 2))
            if self.rank - 1 >= 0 and (board[self.rank - 1][self.column - 2] is None or board[self.rank - 1][self.column - 2].color != self.color):
                res.append((self.rank - 1, self.column - 2))

        #down
        if self.rank - 2 >= 0:
            if self.column + 1 <= 7 and (board[self.rank - 2][self.column + 1] is None or board[self.rank - 2][self.column + 1].color != self.color):
                res.append((self.rank - 2, self.column + 1))
            if self.column - 1 >= 0 and (board[self.rank - 2][self.column - 1] is None or board[self.rank - 2][self.column - 1].color != self.color):
                res.append((self.rank - 2, self.column - 1))

        return res