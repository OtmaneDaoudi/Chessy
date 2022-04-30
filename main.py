from Classes.Board import Board


bd = Board()
bd.move_piece((6,4),(4,4))
bd.move_piece((4,4),(3,4))
bd.move_piece((3,4),(2,4))
bd.printBoard()
print(bd.board[2][7].getPossibleMoves(bd.board))

print("white captured pieces : ",bd.white_captures_pieces)
print("black captured pieces : ",bd.black_captures_pieces)

# bd.move_piece((1,3),(3,3))
# bd.move_piece((3,3),(4,3))

# bd.move_piece((6,2),(4,2))

# bd.move_piece((6,4),(4,4))

# bd.move_piece((4,3),(5,4))
# bd.move_piece((5,4),(6,3))

# bd.printBoard(

# )
# bd.move_piece((6,3),(7,2))

# bd.printBoard(