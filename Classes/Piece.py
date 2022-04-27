class Piece:
    #unicide for pieces,used in __str__
    BLACK_PAWN   = "\u265F"
    BLACK_ROOK   = "\u265C"
    BLACK_KNIGHT = "\u265E"
    BLACK_BISHOP = "\u265D"
    BLACK_QUEEN  = "\u265B"
    BLACK_KING   = "\u265A"

    WHITE_PAWN   = "\u2659"
    WHITE_ROOK   = "\u2656"
    WHITE_KNIGHT = "\u2658"
    WHITE_BISHOP = "\u2657"
    WHITE_QUEEN  = "\u2655"
    WHITE_KING   = "\u2654"

    def __init__(self,rank,column,color,image = None,isKilled = False):
        self.rank = rank
        self.column = column
        self.color = color
        self.isKIlled = isKilled
        self.image = image

    def setPosition(self,newPos):
        self.rank = newPos[0]
        self.column = newPos[1]

