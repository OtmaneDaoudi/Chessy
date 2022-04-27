from Classes.Piece import Piece


class Pawn(Piece):
    def __init__(self,rank,column,color,image = None,isKilled = False,isFirstMove = True) : 
        super().__init__(rank,column,color,image,isKilled)
        self.isFirstMove = isFirstMove
    
    #retrieve all possible moves
    def getPossibleMoves(self,board) -> list: 
        res = []
        if self.color == "w":
            if board[self.rank+1][self.column] == None:
                    res.append((self.rank+1,self.column))
                    if self.isFirstMove and board[self.rank+2][self.column] == None:
                        res.append((self.rank+2,self.column))
        elif  self.color == "b":
            if board[self.rank-1][self.column] == None:
                    res.append((self.rank-1,self.column))
                    if self.isFirstMove and board[self.rank-1][self.column] == None:
                        res.append((self.rank-2,self.column))
        return res

    def Capture(piece):
        pass

    def __str__(self):
        if  (self.color == "w"): return f"{Piece.WHITE_PAWN}"
        elif(self.color == "b"): return f"{Piece.BLACK_PAWN}"
        else :return ""

    def setPosition(self, newPos):
        super().setPosition(newPos)
        # print("sub : setPos")
        if self.isFirstMove == True: self.isFirstMove = False