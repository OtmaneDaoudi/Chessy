from Classes.Piece import Piece


class Pawn(Piece):
    def __init__(self, rank, column, color, image="pawn.png",isFirstMove=True,isPromotable=False):
        super().__init__(rank, column, color, image)
        self.isFirstMove = isFirstMove
        self.isPromotable = isPromotable
        self.countMoves = 0 #used to update the value of isFirstMove
        self.forwardMoveOffset = 0 #this attribute is used to detect en passant captures

    # retrieve all possible moves including captures
    # all moves should not cause team's king ti be under check 
    def getPossibleMoves(self, board) -> list:
        res = []
        if self.color == "w" and not self.isPromotable:
            # print(f"pawn py : self.rank + 1 = {self.rank + 1} ** self.column = {self.column} ** promotable = {self.isPromotable}")
            if board[self.rank + 1][self.column] is None:
                res.append((self.rank + 1, self.column))
                if self.isFirstMove and board[self.rank + 2][self.column] is None:
                    res.append((self.rank + 2, self.column))
            #check diagonals for possible captures
            #check right diagonal
            if self.column < 7 and self.checkSquare(board,self.rank + 1,self.column + 1):
                    res.append((self.rank + 1,self.column + 1))
            #check left diagonal
            if self.column > 0 and self.checkSquare(board,self.rank + 1,self.column -1):
                    res.append((self.rank + 1,self.column - 1))
                
        elif self.color == "b" and not self.isPromotable:
            if board[self.rank - 1][self.column] is None:
                res.append((self.rank - 1, self.column))
                if self.isFirstMove and board[self.rank - 2][self.column] is None:
                    res.append((self.rank - 2, self.column))
            #check diagonals for possible captures
            #check right diagonal
            if self.column < 7 and self.checkSquare(board,self.rank - 1,self.column + 1):
                    res.append((self.rank - 1,self.column + 1))
            #check left diagonal
            if self.column > 0 and self.checkSquare(board,self.rank - 1,self.column - 1):
                    res.append((self.rank - 1,self.column - 1))
        return res

    def checkSquare(self,board,rank,column):
        return board[rank][column] is not None and board[rank][column].color != self.color

    def getPossibleEnPassantCaptures(self,board):
        res = {}
        #check right diagonal en passant moves
        if self.column < 7 :
            targetObject = board[self.rank][self.column + 1]
            if targetObject is not None and isinstance(targetObject,Pawn) and targetObject.color != self.color and targetObject.forwardMoveOffset == 2:
                if self.color == "w":
                        res[(self.rank + 1,self.column + 1)] = (self.rank,self.column + 1) #map each en passant move its captures piece as {move : capture}
                if self.color == "b":
                        res[(self.rank - 1,self.column + 1)] = (self.rank,self.column + 1)
        #check left diagonal en passant moves
        if self.column > 0:
                targetObject = board[self.rank][self.column - 1]
                if targetObject is not None and isinstance(targetObject,Pawn) and targetObject.color != self.color and targetObject.forwardMoveOffset == 2:
                    if self.color == "w":
                        res[(self.rank + 1,self.column - 1)] = (self.rank,self.column - 1)
                    if self.color == "b":
                        res[(self.rank - 1,self.column - 1)] = (self.rank,self.column - 1)
        return res

    def __str__(self):
        if self.color == "w":
            return f"{Piece.WHITE_PAWN}"
        elif self.color == "b":
            return f"{Piece.BLACK_PAWN}"
        else:
            return ""

    def setPosition(self, newPos):
        self.forwardMoveOffset = abs(self.rank - newPos[0])
        super().setPosition(newPos)
        if self.isFirstMove:
            self.isFirstMove = False
        #if the pawn moves to rank 0 or 7 ==> promotable
        if newPos[0] == 0 or newPos[0] == 7:
            self.isPromotable = True