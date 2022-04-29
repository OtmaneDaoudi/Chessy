from Classes.Piece import Piece


class Pawn(Piece):
    def __init__(self, rank, column, color, image=None,isFirstMove=True,isPromotable=False):
        super().__init__(rank, column, color, image)
        self.isFirstMove = isFirstMove
        self.isPromotable = isPromotable

    # retrieve all possible moves including captures
    def getPossibleMoves(self, board) -> list:
        res = []
        if self.color == "w" and not self.isPromotable:
            if board[self.rank + 1][self.column] is None:
                res.append((self.rank + 1, self.column))
                if self.isFirstMove and board[self.rank + 2][self.column] is None:
                    res.append((self.rank + 2, self.column))
            #check diagonals for possible captures
            #if not self.isPromotable : #has not yet reached rank 0 or 7
            #check right diagonal
            if self.column < 7 and board[self.rank + 1][self.column + 1] is not None and board[self.rank + 1][self.column + 1].color != self.color:
                res.append((self.rank + 1,self.column + 1))
            #check left diagonal
            if self.column > 0 and board[self.rank + 1][self.column -1] is not None and board[self.rank + 1][self.column - 1].color != self.color:
               res.append((self.rank + 1,self.column - 1))

        elif self.color == "b" and not self.isPromotable:
            if board[self.rank - 1][self.column] is None:
                res.append((self.rank - 1, self.column))
                if self.isFirstMove and board[self.rank - 1][self.column] is None:
                    res.append((self.rank - 2, self.column))
            #check diagonals for possible captures
            #if not self.isPromotable : #has not yet reached rank 0 or 7
            #check right diagonal
            if self.column < 7 and board[self.rank - 1][self.column + 1] is not None and board[self.rank - 1][self.column + 1].color != self.color:
                res.append((self.rank - 1,self.column + 1))
            #check left diagonal
            if self.column > 0 and board[self.rank - 1][self.column - 1] is not None and board[self.rank + 1][self.column - 1].color != self.color:
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
            #invoke promotion
            self.isPromotable = True

            
