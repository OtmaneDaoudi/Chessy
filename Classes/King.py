from Classes.Piece import Piece


class King(Piece):
    def __init__(self,rank,column,color,image = None,isKilled = False) : 
        super().__init__(rank,column,color,image,isKilled)

    def __str__(self):
        if  (self.color == "w"): return f"{Piece.WHITE_KING}"
        elif(self.color == "b"): return f"{Piece.BLACK_KING}"
        else :return ""