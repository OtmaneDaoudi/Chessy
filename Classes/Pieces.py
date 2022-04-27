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

        def setRank(newRank):
            self.rank = rank

        def setColumn(newColumn):
            self.column = column

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

class Rook(Piece):
    def __init__(self,rank,column,color,image = None,isKilled = False) : 
        super().__init__(rank,column,color,image,isKilled)

    def __str__(self):
        if  (self.color == "w"): return f"{Piece.WHITE_ROOK}"
        elif(self.color == "b"): return f"{Piece.BLACK_ROOK}"
        else :return ""

class Knight(Piece):
    def __init__(self,rank,column,color,image = None,isKilled = False) : 
        super().__init__(rank,column,color,image,isKilled)

    def __str__(self):
        if  (self.color == "w"): return f"{Piece.WHITE_KNIGHT}"
        elif(self.color == "b"): return f"{Piece.BLACK_KNIGHT}"
        else :return ""

class Bishop(Piece):
    def __init__(self,rank,column,color,image = None,isKilled = False) : 
        super().__init__(rank,column,color,image,isKilled)

    def __str__(self):
        if  (self.color == "w"): return f"{Piece.WHITE_BISHOP}"
        elif(self.color == "b"): return f"{Piece.BLACK_BISHOP}"
        else :return ""

class Queen(Piece):
    def __init__(self,rank,column,color,image = None,isKilled = False) : 
        super().__init__(rank,column,color,image,isKilled)

    def __str__(self):
        if  (self.color == "w"): return f"{Piece.WHITE_QUEEN}"
        elif(self.color == "b"): return f"{Piece.BLACK_QUEEN}"
        else :return ""

class King(Piece):
    def __init__(self,rank,column,color,image = None,isKilled = False) : 
        super().__init__(rank,column,color,image,isKilled)

    def __str__(self):
        if  (self.color == "w"): return f"{Piece.WHITE_KING}"
        elif(self.color == "b"): return f"{Piece.BLACK_KING}"
        else :return ""