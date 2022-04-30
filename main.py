from Classes.Board import Board


bd = Board()
bd.printBoard()
print(bd.board[0][1].getPossibleMoves(bd.board))
