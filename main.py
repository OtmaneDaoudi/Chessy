from Classes.Board import Board


bd = Board()
bd.move_piece((1,1),(3,1))
bd.move_piece((3,1),(4,1))
bd.move_piece((4,1),(5,1))
bd.move_piece((5,1),(6,2))
bd.printBoard()
bd.move_piece((6,2),(7,1)) #invokes promotion

bd.printBoard()