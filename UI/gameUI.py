from operator import le
from time import sleep
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.image import Image
from functools import partial
from Classes.Game import Game
from Classes.Piece import Piece
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import mainthread
from kivy.clock import Clock

Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '630')
Config.set('graphics', 'resizable', False)
Config.write()

class Cell(ToggleButton):
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
        if self.piece is not None:
            self.img = Image(source="./Assets/"+self.piece.image)
            self.img.size_hint = (None,None)
            self.img.allow_stretch = True
            self.img.pos = [self.pos[0] + 2.5, self.pos[1] + 3]
            self.img.size = (70,70)
            self.add_widget(self.img)
        else:
            self.img = Image(source="")

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

        # Clock.schedule_once(self.game.start_game, 1)

    def update_board(self):
        self.clear_widgets()
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
        
    def selected(self, rank, column, cell: Cell):
        if cell.piece is None:
            if (rank,column) in self.marked_moved:
                self.game.game_board.move_piece((self.selected_cell.rank,self.selected_cell.column),(rank,column))
                self.update_board()
                self.selected_cell.state = "normal"
                self.selected_cell = None
                for oldTarget in self.marked_moved:
                    self.cells[oldTarget[0]][oldTarget[1]].state = "normal"

            else:
                cell.state = "normal"

        elif cell == self.selected_cell:
            cell.state = "down"

        elif cell.piece.color != self.game.turn:
            if (rank,column) in self.marked_moved:
                self.game.game_board.move_piece((self.selected_cell.rank,self.selected_cell.column),(rank,column))
                self.update_board()
                self.selected_cell.state = "normal"
                self.selected_cell = None
                for oldTarget in self.marked_moved:
                    self.cells[oldTarget[0]][oldTarget[1]].state = "normal"
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