from Classes.Bishop import Bishop
from Classes.Piece import Piece
from Classes.Rook import Rook

class Queen(Piece):
    def __init__(self,rank,column,color,image = None) : 
        super().__init__(rank,column,color,image)

    def __str__(self):
        if  (self.color == "w"): return f"{Piece.WHITE_QUEEN}"
        elif(self.color == "b"): return f"{Piece.BLACK_QUEEN}"
        else :return ""

    def getPossibleMoves(self,board):
        res = []
        #the queen combines the moves of both a rook and a bishop
        as_rook = Rook(self.rank, self.column, self.color)
        as_bishop = Bishop(self.rank , self.column, self.color)
        res.extend(as_rook.getPossibleMoves(board))
        res.extend(as_bishop.getPossibleMoves(board))
        return res