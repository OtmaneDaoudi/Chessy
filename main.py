from Classes.Board import Board


bd = Board()
bd.printBoard()
print(bd.board[1][0].getPossibleMoves(bd.board))
# bd.move_piece((1,0),(5,0))
bd.printBoard()