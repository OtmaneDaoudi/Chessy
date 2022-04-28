from Classes.Piece import Piece


class Pawn(Piece):
    def __init__(self, rank, column, color, image=None, isKilled=False, isFirstMove=True,isPromotable=False):
        super().__init__(rank, column, color, image, isKilled)
        self.isFirstMove = isFirstMove

    # retrieve all possible moves including captures
    def getPossibleMoves(self, board) -> list:
        res = []
        if self.color == "w":
            if board[self.rank + 1][self.column] is None:
                res.append((self.rank + 1, self.column))
                if self.isFirstMove and board[self.rank + 2][self.column] is None:
                    res.append((self.rank + 2, self.column))
            #check diagonals for possible captures
            if not self.isPromotable :
                #check right diagonal
                if self.column < 7 and board[self.rank + 1][self.column + 1].color == "w":
                    res.append((self.rank + 1,self.column + 1))
                #check left diagonal
                if self.column > 0 :
                    res.append((self.rank + 1,self.column - 1))

        elif self.color == "b":
            if board[self.rank - 1][self.column] is None:
                res.append((self.rank - 1, self.column))
                if self.isFirstMove and board[self.rank - 1][self.column] is None:
                    res.append((self.rank - 2, self.column))
            #check diagonals
            if not self.isPromotable :
                #check right diagonal
                if self.column < 7:
                    res.append((self.rank - 1,self.column + 1))
                #check left diagonal
                if self.column > 0 :
                    res.append((self.rank - 1,self.column - 1))
        return res

    def Capture(self, piece):
        pass

    def __str__(self):
        if self.color == "w":
            return f"{Piece.WHITE_PAWN}"
        elif self.color == "b":
            return f"{Piece.BLACK_PAWN}"
        else:
            return ""

    def setPosition(self, newPos):
        super().setPosition(newPos)
        # print("sub : setPos")
        if self.isFirstMove:
            self.isFirstMove = False
        #if the pawn moves to rank 0 or 7 ==> promotable
        if newPos[0] == 0 or newPos[0] == 7:
            self.isPromotable = True
