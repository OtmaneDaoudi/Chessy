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
from kivy.core.audio import SoundLoader
from kivy.animation import Animation

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

        #TODO 
        #if the mode is player vs algorithm
            #if the algorithmis playing first 
                #get a move and perform it

    @mainthread #initilise position in next frame
    def set_img_pos(self):
        if self.piece is not None:
            self.img = Image(source="./Assets/images/"+self.piece.image)
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
        # self.spacing = -2
        self.spacing = 30

        light_square = (124/255.0, 76/255.0, 62/255.0, 1)
        dark_square  = (81/255.0, 42/255.0, 42/255.0, 1)
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

        # Clock.schedule_once(self.game.start_game, 1)

    def update_board(self):
        self.clear_widgets()
        light_square = (124/255.0, 76/255.0, 62/255.0, 1)
        dark_square  = (81/255.0, 42/255.0, 42/255.0, 1)
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

    def animate_move(self,start_cell: Cell, end_cell: Cell):
        ani = Animation(pos=end_cell.pos)
        ani.start(start_cell.img)

        
    def selected(self, rank, column, cell: Cell):
        if cell.piece is None:
            if (rank,column) in self.marked_moved:
                self.game.playMove((self.selected_cell.rank,self.selected_cell.column),(rank,column))
                self.move_piece_sound.play()
                self.update_board()
                self.animate_move(self.selected_cell,cell)
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
                self.game.playMove((self.selected_cell.rank,self.selected_cell.column),(rank,column))
                self.update_board()
                self.animate_move(self.selected_cell,cell)
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
            
        # if self.selected_cell is None:
        #     print("selected cell ==> None")
        # else:
        #     print(f"selected cell : {self.selected_cell.piece.rank},{self.selected_cell.piece.column}")
        # print("Marked moves : ",self.marked_moved)