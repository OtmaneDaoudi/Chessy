from Classes.Board import Board


bd = Board()
bd.move_piece((1,4),(2,4))
bd.move_piece((0,4),(1,4))
bd.printBoard()
print(bd.board[1][4].getPossibleMoves(bd.board))