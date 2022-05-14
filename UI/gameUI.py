from threading import main_thread
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.config import Config
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.image import Image
from functools import partial
from Classes.Game import Game
from Classes.Piece import Piece
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import mainthread

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

    @mainthread
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
        self.game = Game()

        self.cols = 8
        self.rows = 9
        self.padding = -1
        self.spacing = -2

        light_square = (242/255.0, 225/255.0, 195/255.0, 1)
        dark_square  = (195/255.0, 160/255.0, 130/255.0, 1)
        current_color = light_square

        self.cells = [] #stores all ui elements
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

    def selected(self, rank, column, cell):
        print(f"selected {rank} {column}")