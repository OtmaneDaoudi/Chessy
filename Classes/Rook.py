from Classes.Piece import Piece


class Rook(Piece):
    def __init__(self,rank,column,color,image = None) : 
        super().__init__(rank,column,color,image)

    def __str__(self):
        if  (self.color == "w"): return f"{Piece.WHITE_ROOK}"
        elif(self.color == "b"): return f"{Piece.BLACK_ROOK}"
        else :return ""

    def getPossibleMoves(self, board) -> list:
        res = []
        #scan up
        current_rank = self.rank + 1
        while(current_rank <= 7 and board[current_rank][self.column] is None):
            res.append((current_rank,self.column))
            current_rank += 1
        if current_rank<=7 and board[current_rank][self.column] is not None and board[current_rank][self.column].color != self.color:
            res.append((current_rank,self.column))

        #scan down
        current_rank = self.rank - 1
        while(current_rank >= 0 and board[current_rank][self.column] is None) :
            res.append((current_rank,self.column))
            current_rank -= 1
        if current_rank>=0 and board[current_rank][self.column] is not None and board[current_rank][self.column].color != self.color:
            res.append((current_rank,self.column))

        #scan right
        current_column = self.column + 1
        while(current_column <= 7 and board[self.rank][current_column] is None) :
            res.append((self.rank,current_column))
            current_column += 1
        if current_column<=7 and board[self.rank][current_column] is not None and board[self.rank][current_column].color != self.color:
                    res.append((self.rank,current_column))
        #scan left
        current_column = self.column - 1
        while(current_column >= 0 and board[self.rank][current_column] is None) :
            res.append((self.rank,current_column))
            current_column -= 1
        if current_column>=0 and board[self.rank][current_column] is not None and board[self.rank][current_column].color != self.color:
            res.append((self.rank,current_column))

        return res 