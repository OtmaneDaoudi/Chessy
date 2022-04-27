#board squares are mapped to list indexes
#each square has color + rank,column position + piece
from Classes.Piece import Piece
from Classes.Pawn import Pawn
from Classes.Rook import Rook
from Classes.Bishop import Bishop
from Classes.Knight import Knight
from Classes.Queen import Queen
from Classes.King import King
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


    def __init__(self):
        #initialise board
        self.board = []
        for line in range(8):
            self.board.append([None,None,None,None,None,None,None,None])

        # print(self.board)

        #initialise pawns
        #black pawns 
        self.board[1][0] = Pawn(1,0,"w")
        self.board[1][1] = Pawn(1,1,"w")
        self.board[1][2] = Pawn(1,2,"w")
        self.board[1][3] = Pawn(1,3,"w")
        self.board[1][4] = Pawn(1,4,"w")
        self.board[1][5] = Pawn(1,5,"w")
        self.board[1][6] = Pawn(1,6,"w")
        self.board[1][7] = Pawn(1,7,"w")

        #white pawns
        self.board[6][0] = Pawn(6,0,"b")
        self.board[6][1] = Pawn(6,1,"b")
        self.board[6][2] = Pawn(6,2,"b")
        self.board[6][3] = Pawn(6,3,"b")
        self.board[6][4] = Pawn(6,4,"b")
        self.board[6][5] = Pawn(6,5,"b")
        self.board[6][6] = Pawn(6,6,"b")
        self.board[6][7] = Pawn(6,7,"b")

        #initialise rooks
        #black rooks
        self.board[0][0] = Rook(0,0,"w")
        self.board[0][7] = Rook(0,7,"w")
        #white rooks
        self.board[7][0] = Rook(7,0,"b")
        self.board[7][7] = Rook(7,7,"b")


        #initialise knights
        #black knights
        self.board[0][1] = Knight(0,1,"w")
        self.board[0][6] = Knight(0,6,"w")
        #white knights
        self.board[7][1] = Knight(7,1,"b")
        self.board[7][6] = Knight(7,6,"b")

        #initialise Bishops
        #black bishops
        self.board[0][2] = Bishop(0,2,"w")
        self.board[0][5] = Bishop(0,5,"w")
        #white bishops
        self.board[7][2] = Bishop(7,2,"b")
        self.board[7][5] = Bishop(7,5,"b")

        #intialize Queens
        #black Queen
        self.board[0][3] = Queen(0,3,"w")
        #white queen
        self.board[7][3] = Queen(7,3,"b")

        #initilize kings
        #black king
        self.board[0][4] = King(0,4,"w")
        #white king
        self.board[7][4] = King(7,4,"b")

    def printBoard(self):
        for line in reversed(range(8)):
            print("\n  -----------------------------------------")
            print(f"{line+1} |",end="")
            for column in range(8):
                if self.board[line][column] != None:
                    print(f" {self.board[line][column]}  |",end="")
                else : 
                    print("    |",end="")                    
        print("\n  -----------------------------------------")
        print("     A    B    C    D    E    F    G    H") 


    def move_piece(self,start_pos,end_pos):
        if end_pos in self.board[start_pos[0]][start_pos[1]].getPossibleMoves(self.board): 
            #move the piece on baord
            self.board[end_pos[0]][end_pos[1]] = self.board[start_pos[0]][start_pos[1]]
            self.board[start_pos[0]][start_pos[1]] = None
            #update the piece's internal position
            self.board[end_pos[0]][end_pos[1]].setPosition((end_pos[0],end_pos[1]))
        else: print("illegal Move")


    def getPieceByPosition(self) -> Piece:
        pass
