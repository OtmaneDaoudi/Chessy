from Classes.Piece import Piece


class Knight(Piece):
    def __init__(self,rank,column,color,image = "knight.png") : 
        super().__init__(rank,column,color,image)

    def __str__(self):
        if  (self.color == "w"): return f"{Piece.WHITE_KNIGHT}"
        elif(self.color == "b"): return f"{Piece.BLACK_KNIGHT}"
        else :return ""

    def getPossibleMoves(self,board):
        res = []
        #the code bellow can be optimised by creatign a function that does all the repeating stuff
        #up
        if self.rank + 2 <= 7:
            if self.column + 1 <= 7 and self.checkSquare(self.rank + 2,self.column + 1,board):
                res.append((self.rank + 2, self.column + 1))
            if self.column - 1 >= 0 and self.checkSquare(self.rank + 2,self.column - 1,board):
                res.append((self.rank + 2, self.column - 1))

        #right
        if self.column + 2 <= 7:
            if self.rank + 1 <= 7 and self.checkSquare(self.rank + 1,self.column + 2,board):
                res.append((self.rank + 1,self.column + 2))
            if self.rank - 1 >= 0 and self.checkSquare(self.rank - 1,self.column + 2,board):
                res.append((self.rank - 1, self.column + 2))

        #left
        if self.column - 2 >= 0:
            if self.rank + 1 <= 7 and self.checkSquare(self.rank + 1, self.column -2, board):
                res.append((self.rank + 1, self.column - 2))
            if self.rank - 1 >= 0 and self.checkSquare(self.rank - 1, self.column - 2, board):
                res.append((self.rank - 1, self.column - 2))

        #down
        if self.rank - 2 >= 0:
            if self.column + 1 <= 7 and self.checkSquare(self.rank - 2, self.column + 1, board):
                res.append((self.rank - 2, self.column + 1))
            if self.column - 1 >= 0 and self.checkSquare(self.rank - 2, self.column - 1, board):
                res.append((self.rank - 2, self.column - 1))
        return res

    def checkSquare(self,rank,column,board):
        return (board[rank][column] is None or board[rank][column].color != self.color)