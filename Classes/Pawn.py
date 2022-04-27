from Classes.Piece import Piece


class Pawn(Piece):
    def __init__(self,rank,column,color,image = None,isKilled = False) : 
        super().__init__(rank,column,color,image,isKilled)
    
    def getPossibleMoves(self):
        pass

    def Capture(piece):
        pass

    def __str__(self):
        if  (self.color == "w"): return f"{Piece.WHITE_PAWN}"
        elif(self.color == "b"): return f"{Piece.BLACK_PAWN}"
        else :return ""