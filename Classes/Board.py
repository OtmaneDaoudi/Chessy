# board squares are mapped to list indexes
# each square has color + rank,column + piece
# each piece contains a reference to a valid piece subClass instance or None in case of empty
from Classes.Pawn import Pawn
from Classes.Rook import Rook
from Classes.Bishop import Bishop
from Classes.Knight import Knight
from Classes.Queen import Queen
from Classes.King import King
from copy import deepcopy


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

        # # black pawns
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
        print("="*43)
        # print(f"white's king position : {self.white_king_position}")
        # print(f"black's king position : {self.black_king_position}")
        print(f"pieces captured by white : {self.white_captures_pieces}")
        print(f"pieces captured by black : {self.black_captures_pieces}")
        r1 = self.isCheckMate("b")
        print(f"is black checkmate = {r1}")
        r2 = self.isCheckMate("w")
        print(f"is white check = {r2}")
        r3 = self.isCheck("w")
        print(f"is white check = {r3}")
        r4 = self.isCheck("b")
        print(f"is black check = {r4}")
        print("="*43)


    #move piece and update the position of the piece
    #when moving a pawn we need to check for promotion 
    #when a king is under check , the player is forced to resolve the check , otherwise a checkmate happens
    def move_piece(self, start_pos: tuple, end_pos : tuple) -> bool: #,turn : str):
        isMoved = False
        #is it a valid move + the move will not cause me check
        if end_pos in self.board[start_pos[0]][start_pos[1]].getPossibleMoves(self.board) and not self.MoveCauseCheck(start_pos,end_pos):  
            # move the piece on baord
            if self.board[end_pos[0]][end_pos[1]] is not None : #capture detected
                print("capture") #log all captures
                #capture piece and append it to the captures pieces list
                if self.board[end_pos[0]][end_pos[1]].color == "b": 
                    self.white_captures_pieces.append(self.board[end_pos[0]][end_pos[1]])
                elif self.board[end_pos[0]][end_pos[1]].color == "w":
                    self.black_captures_pieces.append(self.board[end_pos[0]][end_pos[1]])

            #update the board
            self.board[end_pos[0]][end_pos[1]] = self.board[start_pos[0]][start_pos[1]]
            self.board[start_pos[0]][start_pos[1]] = None
            # update the piece's internal position
            self.board[end_pos[0]][end_pos[1]].setPosition((end_pos[0], end_pos[1]))
    
            #if king is moved update board's king positions
            if isinstance(self.board[end_pos[0]][end_pos[1]],King):
                print("king move detected, king indexes updated")
                if self.board[end_pos[0]][end_pos[1]].color == "b":
                    self.black_king_position = end_pos
                else:
                    self.white_king_position = end_pos

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

        #detect castling moves
        elif isinstance(self.board[start_pos[0]][start_pos[1]],King):
            if end_pos in self.getPossibleCastleMoves(self.board[start_pos[0]][start_pos[1]].color):
                print("castel move detected")
                #swap king and rook
                if end_pos[1] == 6: #king side castling
                    if self.board[start_pos[0]][start_pos[1]].color == "w": #white king side castling
                        self.board[0][6] = self.board[start_pos[0]][start_pos[1]]
                        self.board[start_pos[0]][start_pos[1]] = None
                        self.board[0][6].setPosition((0,6))
                        self.white_king_position = (0,6)

                        self.board[0][5] = self.board[0][7]
                        self.board[0][7] = None
                        self.board[0][5].setPosition((0,5))                        
                    else : #black king side castling
                        self.board[7][6] = self.board[start_pos[0]][start_pos[1]]
                        self.board[start_pos[0]][start_pos[1]] = None
                        self.board[7][6].setPosition((7,6))
                        self.black_king_position = (7,6)

                        self.board[7][5] = self.board[7][7]
                        self.board[7][7] = None
                        self.board[7][5].setPosition((7,5))
                else:
                    if self.board[start_pos[0]][start_pos[1]].color == "w": #white queen side castling
                        self.board[0][2] = self.board[start_pos[0]][start_pos[1]]
                        self.board[start_pos[0]][start_pos[1]] = None
                        self.board[0][0].setPosition((0,2))
                        self.white_king_position = (0,2)

                        self.board[0][3] = self.board[0][0]
                        self.board[0][0] = None
                        self.board[0][3].setPosition((0,3))
                    else :
                        self.board[7][2] = self.board[start_pos[0]][start_pos[1]]
                        self.board[start_pos[0]][start_pos[1]] = None
                        self.board[7][0].setPosition((7,2))
                        self.black_king_position = (7,2)

                        self.board[7][3] = self.board[7][0]
                        self.board[7][0] = None
                        self.board[7][3].setPosition((7,3))
                isMoved = True       
                    
        return isMoved

    def MoveCauseCheck(self,start_pos: tuple,end_pos: tuple) -> bool:
        #create new local instance of the board
        cloned_board = deepcopy(self)
        #simulate the move in the new board
        #update the board
        cloned_board.board[end_pos[0]][end_pos[1]] = cloned_board.board[start_pos[0]][start_pos[1]]
        cloned_board.board[start_pos[0]][start_pos[1]] = None
        cloned_board.board[end_pos[0]][end_pos[1]].setPosition((end_pos[0], end_pos[1]))

        #if king is moved update board's king positions
        if isinstance(cloned_board.board[end_pos[0]][end_pos[1]],King):
            if cloned_board.board[end_pos[0]][end_pos[1]].color == "b":
                cloned_board.black_king_position = end_pos
            else:
                cloned_board.white_king_position = end_pos
        #loop over all other team pieces and see if my king is in thier possible moves
        my_color = cloned_board.board[end_pos[0]][end_pos[1]].color

        return cloned_board.isCheck(my_color)

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

    #checks for king checks + checkmates
    def isCheck(self,color) -> bool: 
        #a player is in check mate when he is under check + he has no legal moves that will resolve the check
        #-1 ==> no check , 0 ==> color team is under check , 1 ==> color teams trapped under checkMate ==> other team wins
        #check if a given team's king is underCheck
        #loop over all other teams pieces and return if my king is in thier possible moves
        other_team_possible_moves = []
        for line in range(len(self.board)):
            for column in range(len(self.board[line])):
                if self.board[line][column] is not None and self.board[line][column].color != color:
                    other_team_possible_moves.extend(self.board[line][column].getPossibleMoves(self.board))

        return  (color == "w" and self.white_king_position in other_team_possible_moves) or (color == "b" and self.black_king_position in other_team_possible_moves) 

    def isCheckMate(self,color) -> bool:
        #checkmate = check + no legal moves
        if self.isCheck(color) :     
            #check if the player has no legal moves that will resolve the check 
            for line in range(len(self.board)):
                for column in range(len(self.board[line])):
                    if self.board[line][column] is not None and self.board[line][column].color == color:
                        possibleEndMoves = self.board[line][column].getPossibleMoves(self.board)
                        if isinstance(self.board[line][column],Pawn):
                            possibleEndMoves.extend(list(self.board[line][column].getPossibleEnPassantCaptures(self.board).keys()))
                        if isinstance(self.board[line][column],King):
                            self.getPossibleCastleMoves(self.board[line][column].color)
                        possibleEndMoves.getPossibleCastleMoves()
                        for move in possibleEndMoves:
                            if not self.MoveCauseCheck((line,column),move):
                                return False
                        return True
        return False
        
    def isStaleMate(self,color) -> bool:
        #a stalemate happens when 
        # 1-it's my turn to play --ensured by the caller
        # 2-my king is not in check  --ensured by the caller
        # 3-i have no legal moves for any of my pieces
        available_moves = []
        for line in range(len(self.board)):
            for column in range(len(self.board[line])):
                if self.board[line][column] is not None and self.board[line][column].color == color:
                    for move in self.board[line][column].getPossibleMoves(self.board):
                        if not self.MoveCauseCheck((line,column),move):
                            available_moves.extend(move)
        return not (len(available_moves) > 0)

    #if a move is returned ==> all clear to castle
    def getPossibleCastleMoves(self,color):
        res = []
        if color == "w":
            if not self.board[self.white_king_position[0]][self.white_king_position[1]].isMoved and not self.isCheck("w"): #king not in check and hasen't moved yet
                #check king side castling availability
                if self.board[0][7] is not None and not self.board[0][7].isMoved: #if the king side rook hasen't moved yet too
                    if self.board[0][5] is None and self.board[0][6] is None : #if every thing is clear
                        #check if crossing the squares will not raise a check
                        if not self.MoveCauseCheck(self.white_king_position,(0,5)): #if the first square crossed is fine
                            cloned_board = deepcopy(self)
                            #move king in cloned board
                            cloned_board.board[0][5] = cloned_board.board[0][4]
                            cloned_board.board[0][4] = None
                            # update the piece's internal position
                            cloned_board.board[0][5].setPosition((0,5))
                            if not cloned_board.MoveCauseCheck((0,5),(0,6)) : #all clear
                                res.append((0,6))
                #check Queen side csatling availability
                if self.board[0][0] is not None and not self.board[0][0].isMoved: #queen side rook hasen't moved
                    if self.board[0][3] is None and self.board[0][2] is None and self.board[0][1] is None : #all clear to move
                        #check if the crossing squres will not cause 
                        if not self.MoveCauseCheck(self.white_king_position,(0,3)): #if the first square crossed is fine
                            cloned_board = deepcopy(self)
                            #move king in cloned board
                            cloned_board.board[0][3] = cloned_board.board[0][4]
                            cloned_board.board[0][4] = None
                            # update the piece's internal position
                            cloned_board.board[0][3].setPosition((0,3))
                            if not cloned_board.MoveCauseCheck((0,3),(0,2)) : #all clear
                                res.append((0,2))
        else :
            if not self.board[self.black_king_position[0]][self.black_king_position[1]].isMoved and not self.isCheck("b"): #king not in check and hasen't moved yet
                #check king side castling availability
                if self.board[7][7] is not None and not self.board[7][7].isMoved: #if the king side rook hasen't moved yet too
                    if self.board[7][5] is None and self.board[7][6] is None : #if every thing is clear
                        #check if crossing the squares will not raise a check
                        if not self.MoveCauseCheck(self.black_king_position,(7,5)): #if the first square crossed is fine
                            cloned_board = deepcopy(self)
                            #move king in cloned board
                            cloned_board.board[7][5] = cloned_board.board[7][4]
                            cloned_board.board[7][4] = None
                            # update the piece's internal position
                            cloned_board.board[7][5].setPosition((7,5))
                            if not cloned_board.MoveCauseCheck((7,5),(7,6)) : #all clear
                                res.append((7,6))
                #check Queen side csatling availability
                if self.board[7][0] is not None and not self.board[7][0].isMoved: #queen side rook hasen't moved
                    if self.board[7][3] is  None and self.board[7][2] is None and self.board[7][1] is None : #all clear to move
                        #check if the crossing squres will not cause 
                        if not self.MoveCauseCheck(self.black_king_position,(7,3)): #if the first square crossed is fine
                            cloned_board = deepcopy(self)
                            #move king in cloned board
                            cloned_board.board[7][3] = cloned_board.board[7][4]
                            cloned_board.board[7][4] = None
                            # update the piece's internal position
                            cloned_board.board[7][3].setPosition((7,3))
                            if not cloned_board.MoveCauseCheck((7,3),(7,2)) : #all clear
                                res.append((7,2))
        return res