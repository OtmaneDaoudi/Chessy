from Classes.Piece import Piece


class Bishop(Piece):
    def __init__(self,rank,column,color,image = "bishop.png") : 
        super().__init__(rank,column,color,image)

    def __str__(self):
        if  (self.color == "w"): return f"{Piece.WHITE_BISHOP}"
        elif(self.color == "b"): return f"{Piece.BLACK_BISHOP}"
        else :return ""

    def getPossibleMoves(self,board) -> list:
        res = []
        #scan top right diagonal 
        current_rank,current_column = self.rank + 1, self.column + 1
        while(current_rank <= 7 and current_column <= 7):
            if board[current_rank][current_column] is None:
                res.append((current_rank,current_column))
            elif board[current_rank][current_column].color != self.color:
                res.append((current_rank,current_column))
                break
            else:
                break
            current_rank += 1
            current_column += 1
        #scan top left diagonal
        current_rank,current_column = self.rank + 1, self.column - 1
        while(current_rank <= 7 and current_column >= 0):
            if board[current_rank][current_column] is None:
                res.append((current_rank,current_column))
            elif board[current_rank][current_column].color != self.color:
                res.append((current_rank,current_column))
                break
            else:
                break
            current_rank += 1
            current_column -= 1
        #scan bottom right diagonal
        current_rank,current_column = self.rank - 1, self.column + 1
        while(current_rank >= 0 and current_column <= 7):
            if board[current_rank][current_column] is None:
                res.append((current_rank,current_column))
            elif board[current_rank][current_column].color != self.color:
                res.append((current_rank,current_column))
                break
            else:
                break
            current_rank -= 1
            current_column += 1
        #scan bottom left diagonal
        current_rank,current_column = self.rank - 1, self.column - 1
        while(current_rank >= 0 and current_column >= 0):
            if board[current_rank][current_column] is None:
                res.append((current_rank,current_column))
            elif board[current_rank][current_column].color != self.color:
                res.append((current_rank,current_column))
                break
            else:
                break
            current_rank -= 1
            current_column -= 1
        return res
