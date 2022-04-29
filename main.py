from Classes.Board import Board


bd = Board()
bd.printBoard()
bd.move_piece((1,0),(3,0))
bd.move_piece((3,0),(4,0))
bd.move_piece((6,1),(4,1))
bd.printBoard()
bd.move_piece((1,7),(3,7))
# bd.move_piece((4,0),(5,1)) #illegal
bd.move_piece((3,7),(4,7))
bd.move_piece((6,6),(4,6))

bd.move_piece((4,7),(5,6))
# print(bd.board[4][1].getPossibleMoves(bd.board))
# bd.move_piece((4,0),(5,1)) #bug
bd.move_piece((6,5),(5,6))

print("white pieces : ",bd.white_captures_pieces)
print("black pieces : ",bd.black_captures_pieces)
bd.printBoard()