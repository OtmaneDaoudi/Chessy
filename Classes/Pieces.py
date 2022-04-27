class Piece:
    def __init__(self,rank,column,color,image = None,isKilled = False):
        self.color = color
        self.isKIlled = isKilled
        self.image = image
        #self.type = type #String representation

class Pawn(Piece):
    def __init__(self,rank,column,color,image = None,isKilled = False) : 
        super().__init__(rank,column,color,image,isKilled)
    
    def getPossibleMoves(self):
        pass

    def Capture(piece):
        pass

class Rook(Piece):
    pass

class Knight(Piece):
    pass

class Bishop(Piece):
    pass

class Queen(Piece):
    pass

class King(Piece):
    pass