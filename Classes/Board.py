# board squares are mapped to list indexes
# each square has color + rank,column + piece
# each piece contains a reference to a valid piece subClass instance or None in case of empty
from xmlrpc.client import Boolean
from Classes.Piece import Piece
from Classes.Pawn import Pawn
from Classes.Rook import Rook
from Classes.Bishop import Bishop
from Classes.Knight import Knight
from Classes.Queen import Queen
from Classes.King import King


class Board:
    def __init__(self):
        # initialise board
        self.board = []
        for line in range(8):
            self.board.append([None, None, None, None, None, None, None, None])

        # initialise pawns
        # white pawns
        self.board[1][0] = Pawn(1, 0, "w")
        self.board[1][1] = Pawn(1, 1, "w")
        self.board[1][2] = Pawn(1, 2, "w")
        self.board[1][3] = Pawn(1, 3, "w")
        self.board[1][4] = Pawn(1, 4, "w")
        self.board[1][5] = Pawn(1, 5, "w")
        self.board[1][6] = Pawn(1, 6, "w")
        self.board[1][7] = Pawn(1, 7, "w")

        # black pawns
        self.board[6][0] = Pawn(6, 0, "b")
        self.board[6][1] = Pawn(6, 1, "b")
        self.board[6][2] = Pawn(6, 2, "b")
        self.board[6][3] = Pawn(6, 3, "b")
        self.board[6][4] = Pawn(6, 4, "b")
        self.board[6][5] = Pawn(6, 5, "b")
        self.board[6][6] = Pawn(6, 6, "b")
        self.board[6][7] = Pawn(6, 7, "b")

        # initialise rooks
        # white rooks
        self.board[0][0] = Rook(0, 0, "w")
        self.board[0][7] = Rook(0, 7, "w")
        # black rooks
        self.board[7][0] = Rook(7, 0, "b")
        self.board[7][7] = Rook(7, 7, "b")

        # initialise knights
        # white knights
        self.board[0][1] = Knight(0, 1, "w")
        self.board[0][6] = Knight(0, 6, "w")
        # black knights
        self.board[7][1] = Knight(7, 1, "b")
        self.board[7][6] = Knight(7, 6, "b")

        # initialise Bishops
        # white bishops
        self.board[0][2] = Bishop(0, 2, "w")
        self.board[0][5] = Bishop(0, 5, "w")
        # black bishops
        self.board[7][2] = Bishop(7, 2, "b")
        self.board[7][5] = Bishop(7, 5, "b")

        # intialize Queens
        # white Queen
        self.board[0][3] = Queen(0, 3, "w")
        # black queen
        self.board[7][3] = Queen(7, 3, "b")

        # initilize kings
        # white king
        self.board[0][4] = King(0, 4, "w")
        self.white_king_position = (0,4)
        # black king
        self.board[7][4] = King(7, 4, "b")
        self.black_king_position = (7,4)

        self.white_captures_pieces = []
        self.black_captures_pieces = []

        #en passant privilage 
        #if one player playes a move the other looses the right for his en passant
        self.LastMovedPiece = None

    def printBoard(self):
        for line in reversed(range(8)):
            print("\n  -----------------------------------------")
            #print(f"{line + 1} |", end="") #print programmer friendly representation
            print(f"{line} |", end="")
            for column in range(8):
                if self.board[line][column] is not None:
                    print(f" {self.board[line][column]}  |", end="")
                else:
                    print("    |", end="")
        print("\n  -----------------------------------------")
        #print("     A    B    C    D    E    F    G    H")
        print("     0    1    2    3    4    5    6    7")

    #move piece and update the position of the piece
    #when moving a pawn we need to check for promotion 
    def move_piece(self, start_pos: tuple, end_pos : tuple): #,turn : str):
        isMoved = False
        if end_pos in self.board[start_pos[0]][start_pos[1]].getPossibleMoves(self.board):  #is it a valid move
            #check if the move will lead to a check
            
            # move the piece on baord
            if self.board[end_pos[0]][end_pos[1]] is not None : #capture detected
                print("capture") #log all captures
                #capture piece and append it to the captures pieces list
                if self.board[end_pos[0]][end_pos[1]].color == "b" : 
                    self.white_captures_pieces.append(self.board[end_pos[0]][end_pos[1]])
                elif self.board[end_pos[0]][end_pos[1]].color == "w":
                    self.black_captures_pieces.append(self.board[end_pos[0]][end_pos[1]])

            #update the board
            self.board[end_pos[0]][end_pos[1]] = self.board[start_pos[0]][start_pos[1]]
            self.board[start_pos[0]][start_pos[1]] = None
            # update the piece's internal position
            self.board[end_pos[0]][end_pos[1]].setPosition((end_pos[0], end_pos[1]))
    
            self.LastMovedPiece = self.board[end_pos[0]][end_pos[1]]
            isMoved = True #marks the piece as moved

            #check for pawn promotion
            if isinstance(self.board[end_pos[0]][end_pos[1]],Pawn):
                if self.board[end_pos[0]][end_pos[1]].isPromotable:
                    self.promotePawn(end_pos)
            

        #detect en passant captures for pawn 
        #en passant happens only in rank 4 and 3 so we can't have promotion + en passant
        elif isinstance(self.board[start_pos[0]][start_pos[1]],Pawn):
            temp_res = self.board[start_pos[0]][start_pos[1]].getPossibleEnPassantCaptures(self.board)
            # print("temp_res : ",temp_res)
            if (end_pos[0],end_pos[1]) in temp_res.keys():
                # print("capturing en passant")
                captured_piece_index = temp_res[(end_pos[0],end_pos[1])]
                if self.board[captured_piece_index[0]][captured_piece_index[1]] == self.LastMovedPiece:
                    print("capturing en passant")
                    self.board[end_pos[0]][end_pos[1]] = self.board[start_pos[0]][start_pos[1]]
                    self.board[start_pos[0]][start_pos[1]] = None
                    self.board[end_pos[0]][end_pos[1]].setPosition((end_pos[0], end_pos[1]))

                    if self.board[end_pos[0]][end_pos[1]].color == "b":
                        self.black_captures_pieces.append(self.board[captured_piece_index[0]][captured_piece_index[1]])
                    else :
                        self.white_captures_pieces.append(self.board[captured_piece_index[0]][captured_piece_index[1]])
                        
                    self.board[captured_piece_index[0]][captured_piece_index[1]] = None
                    
                    self.LastMovedPiece = self.board[end_pos[0]][end_pos[1]]
                    isMoved = True

        if not isMoved : #if no legal move is performaed
            print("illegal Move")

    def MoveCauseCheck(self,start_pos: tuple,end_pos: tuple) -> Boolean:
        res = False
        #create new local instance of the board
        #simulate the move in the new board
        #loop over all other team pieces and see if my king is in thier possible moves
        #return res
        return res

    def getPieceByPosition(self,position : tuple) -> Piece:
        pass

    def promotePawn(self,position : tuple):
        print(f"select which piece to promote pawn at {position} to (k=knight, q=queen, b=bishop, r=rook) >>> ",end="")
        selection = input("")

        if selection in ("k","q","r","b") : 
            old_pawn_color = self.board[position[0]][position[1]].color
            self.board[position[0]][position[1]] = None

            if selection == "k":
                self.board[position[0]][position[1]] = Knight(position[0],position[1],old_pawn_color)
            elif selection == "q":
                self.board[position[0]][position[1]] = Queen(position[0],position[1],old_pawn_color)
            elif selection == "b":
                self.board[position[0]][position[1]] = Bishop(position[0],position[1],old_pawn_color)
            elif selection == "r":
                self.board[position[0]][position[1]] = Rook(position[0],position[1],old_pawn_color)
            self.LastMovedPiece = self.board[position[0]][position[1]]
        else:
            print("enter valid piece name")
            self.promotePawn(position) #reinvoke in case of invalid move