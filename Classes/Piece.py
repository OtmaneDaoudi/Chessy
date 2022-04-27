class Piece:
    #unicide for pieces,used in __str__
    #terminals show inverted colors, edit __str__ in pieces later
    WHITE_PAWN   = "\u265F"
    WHITE_ROOK   = "\u265C"
    WHITE_KNIGHT = "\u265E"
    WHITE_BISHOP = "\u265D"
    WHITE_QUEEN  = "\u265B"
    WHITE_KING   = "\u265A"

    BLACK_PAWN   = "\u2659"
    BLACK_ROOK   = "\u2656"
    BLACK_KNIGHT = "\u2658"
    BLACK_BISHOP = "\u2657"
    BLACK_QUEEN  = "\u2655"
    BLACK_KING   = "\u2654"

    def __init__(self,rank,column,color,image = None,isKilled = False):
        self.rank = rank
        self.column = column
        self.color = color
        self.isKIlled = isKilled
        self.image = image

    def setPosition(self,newPos):
        # print("super: setPos")
        self.rank = newPos[0]
        self.column = newPos[1]