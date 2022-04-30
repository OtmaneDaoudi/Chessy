from Classes.Board import Board


bd = Board()
bd.printBoard()
bd.move_piece((1,3),(3,3))
bd.move_piece((0,3),(1,3))
bd.move_piece((1,3),(2,3))
print(bd.board[2][3].getPossibleMoves(bd.board))
bd.printBoard()
