from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.image import Image
from functools import partial
from Classes.Game import Game
from Classes.Piece import Piece
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import mainthread
from kivy.core.audio import SoundLoader
from kivy.animation import Animation    
from kivy.app import App
from Classes.Knight import Knight
from Classes.Pawn import Pawn
from Classes.Rook import Rook
from Classes.Queen import Queen
from Classes.Bishop import Bishop
from kivy.clock import Clock
# Config.set('graphics', 'width', '900')
# Config.set('graphics', 'height', '630')
# Config.set('graphics', 'resizable', False)
# Config.write()

class Cell(ToggleButton, FloatLayout):
    def __init__(self,rank: int,column: int,color: tuple,piece: Piece,**kwargs):
        super().__init__(**kwargs)
        self.piece = piece
        self.rank = rank
        self.column = column
        self.background_normal=''
        self.background_color = color
        
        self.img = None

    @mainthread #initilise position in next frame
    def set_img_pos(self):
        if self.img is not None:
            self.remove_widget(self.img)
        source_ = "./Assets/images/None.png"
        if self.piece is not None:
            source_ ="./Assets/images/"+self.piece.image
        self.img = Image(source = source_)
        self.img.size_hint = (None,None)
        self.img.allow_stretch = True
        self.img.pos = [self.pos[0] + 2.5, self.pos[1] + 3]
        self.img.size = (70,70)
        self.add_widget(self.img)

class GameUi(BoxLayout):
    pass   

class ChessBoard(GridLayout):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        self.game = Game(self)

        self.selected_cell = None
        self.marked_moved = []

        self.cols = 8
        self.rows = 9
        self.padding = -1
        self.spacing = -2
        # self.spacing = 30

        light_square = (242/255.0, 225/255.0, 195/255.0, 1)
        dark_square  = (195/255.0, 160/255.0, 130/255.0, 1)
        current_color = light_square

        self.cells = [] #stores grid cells
        for _ in range(8):
            self.cells.append([None, None, None, None, None, None, None, None])

        for rank in reversed(range(8)):
            for column in range(8):
                newCell = Cell(rank,column,current_color,self.game.game_board.board[rank][column])
                newCell.on_press = partial(self.selected, rank, column, newCell)
                self.cells[rank][column] = newCell
                self.add_widget(newCell)
                newCell.set_img_pos()
                if current_color == light_square:
                    current_color = dark_square
                else: 
                    current_color = light_square
            if current_color == light_square:
                    current_color = dark_square
            else: 
                current_color = light_square

        self.move_piece_sound = SoundLoader.load('./Assets/audio/piece_move.wav')

        #schedule clock updates
        Clock.schedule_interval(self.game.update_clocks, 1)
        

    def update_board(self):
        for rank in reversed(range(8)):
            for column in range(8):
                oldPiece = self.cells[rank][column].piece 
                self.cells[rank][column].piece = self.game.game_board.board[rank][column]
                if not (oldPiece == self.game.game_board.board[rank][column]):
                    self.cells[rank][column].set_img_pos()

        #update captured pieces
        self.update_score()

    def update_score(self):
        black_ids = App.get_running_app().root.ids.black_captured_pieces.ids
        white_ids = App.get_running_app().root.ids.white_captured_pieces.ids

        #update white pieces           
        pieces_type = list(map(type, self.game.game_board.white_captures_pieces))
        white_ids.pawn.text = str(pieces_type.count(Pawn))
        white_ids.rook.text = str(pieces_type.count(Rook))
        white_ids.bishop.text = str(pieces_type.count(Bishop))
        white_ids.knight.text = str(pieces_type.count(Knight))
        white_ids.queen.text = str(pieces_type.count(Queen))

        #update black pieces           
        pieces_type = list(map(type, self.game.game_board.black_captures_pieces))
        black_ids.pawn.text = str(pieces_type.count(Pawn))
        black_ids.rook.text = str(pieces_type.count(Rook))
        black_ids.bishop.text = str(pieces_type.count(Bishop))
        black_ids.knight.text = str(pieces_type.count(Knight))
        black_ids.queen.text = str(pieces_type.count(Queen))
        

    def animate_move(self,start_cell: Cell, end_cell: Cell):
        ani = Animation(pos=end_cell.pos)
        ani.start(start_cell.img)

        
    def selected(self, rank, column, cell: Cell):
        if cell.piece is None:
            if (rank,column) in self.marked_moved:
                print("self type ",type(self))
                self.game.playMove((self.selected_cell.rank,self.selected_cell.column),(rank,column), self)
                self.move_piece_sound.play()
                self.update_board()
                # self.animate_move(self.selected_cell,cell)
                self.selected_cell.state = "normal"
                self.selected_cell = None
                for oldTarget in self.marked_moved:
                    self.cells[oldTarget[0]][oldTarget[1]].state = "normal"
                self.marked_moved.clear()
            else:
                cell.state = "normal"
        elif cell == self.selected_cell:
            cell.state = "down"
        elif cell.piece.color != self.game.turn:
            if (rank,column) in self.marked_moved:
                self.game.playMove((self.selected_cell.rank,self.selected_cell.column),(rank,column), self)
                self.update_board()
                # self.animate_move(self.selected_cell,cell)
                self.move_piece_sound.play()
                self.selected_cell.state = "normal"
                self.selected_cell = None
                for oldTarget in self.marked_moved:
                    self.cells[oldTarget[0]][oldTarget[1]].state = "normal"
                self.marked_moved.clear()
            else:
                cell.state = "normal"
        else: #clicked on one of my pieces
            if self.selected_cell is None: #no selected pieces
                self.selected_cell = cell
                PossibleMoves = self.game.game_board.getEligableMoves(rank,column)
                self.marked_moved.clear()
                self.marked_moved.extend(PossibleMoves)
                for target in PossibleMoves:
                    self.cells[target[0]][target[1]].state = "down"
            else:
                self.selected_cell.state = "normal"
                self.selected_cell = cell
                for oldTarget in self.marked_moved:
                    self.cells[oldTarget[0]][oldTarget[1]].state = "normal"
                self.marked_moved.clear()
                PossibleMoves = self.game.game_board.getEligableMoves(rank,column)
                self.marked_moved.extend(PossibleMoves)
                for target in PossibleMoves:
                    self.cells[target[0]][target[1]].state = "down"

        print("game status : ",self.game.game_status.name)