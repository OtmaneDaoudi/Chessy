#board squares are mapped to list indexes
#each square has color + rank,column position + piece
from Classes.Pieces import Bishop, King, Knight, Pawn, Queen, Rook
class Board:
    #column mapping 
    # mapping = { "a" : 0,
    #             "b" : 1,
    #             "c" : 2,
    #             "d" : 3,
    #             "e" : 4,
    #             "f" : 5,
    #             "g" : 6,
    #             "h" : 7 }

    #unicide for pieces
    BLACK_PAWN = "U265F"
    BLACK_ROOK = "U265C"
    BLACK_KNIGHT = "U265E"
    BLACK_BISHOP = "U265D"
    BLACK_QUEEN = "U265B"
    BLACK_KING = "U265A"

    WHITE_PAWN = "U2659"
    WHITE_ROOK = "\u2656"
    WHITE_KNIGHT = "U2658"
    WHITE_BISHOP = "U2657"
    WHITE_QUEEN = "U+2655"
    WHITE_KING = "U2654"

    def __init__(self):
        #initialise board
        self.board = []
        for line in range(8):
            self.board.append([None,None,None,None,None,None,None,None])

        # print(self.board)

        #initialise pawns
        #white pawns 
        self.board[1][0] = Pawn(1,0,"w")
        self.board[1][1] = Pawn(1,1,"w")
        self.board[1][2] = Pawn(1,2,"w")
        self.board[1][3] = Pawn(1,3,"w")
        self.board[1][4] = Pawn(1,4,"w")
        self.board[1][5] = Pawn(1,5,"w")
        self.board[1][6] = Pawn(1,6,"w")
        self.board[1][7] = Pawn(1,7,"w")

        #black pawns
        self.board[6][0] = Pawn(6,0,"b")
        self.board[6][1] = Pawn(6,1,"b")
        self.board[6][2] = Pawn(6,2,"b")
        self.board[6][3] = Pawn(6,3,"b")
        self.board[6][4] = Pawn(6,4,"b")
        self.board[6][5] = Pawn(6,5,"b")
        self.board[6][6] = Pawn(6,6,"b")
        self.board[6][7] = Pawn(6,7,"b")

        #initialise rooks
        #white rooks
        self.board[0][0] = Rook(0,0,"w")
        self.board[0][7] = Rook(0,7,"w")
        #black rooks
        self.board[7][0] = Rook(7,0,"b")
        self.board[7][7] = Rook(7,7,"b")


        #initialise knights
        #white knights
        self.board[0][1] = Knight(0,1,"w")
        self.board[0][6] = Knight(0,6,"w")
        #black knights
        self.board[7][1] = Knight(7,1,"b")
        self.board[7][6] = Knight(7,6,"b")

        #initialise Bishops
        #white bishops
        self.board[0][2] = Bishop(0,2,"w")
        self.board[0][5] = Bishop(0,5,"w")
        #black bishops
        self.board[7][2] = Bishop(7,2,"b")
        self.board[7][5] = Bishop(7,5,"b")

        #intialize Queens
        #white Queen
        self.board[0][3] = Queen(0,3,"w")
        #black queen
        self.board[7][3] = Queen(7,3,"b")

        #initilize kings
        #white king
        self.board[0][4] = King(0,4,"w")
        #black king
        self.board[7][4] = King(7,4,"b")

    def printBoard(self):
        print(f"{Board.WHITE_ROOK}")