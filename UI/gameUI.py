from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.config import Config
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.image import Image
from functools import partial

Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'resizable', False)
Config.write()

class Cell(ToggleButton):
    def __init__(self,rank: int,column: int,color: tuple,image_path: str,**kwargs):
        super().__init__(**kwargs)
        self.rank = rank
        self.column = column
        self.background_normal=''
        self.background_color = color

        self.img = Image(source=image_path)
        self.img.size_hint = (None,None)
        self.img.allow_stretch = True
        self.img.pos = (75*column+1.5,75*rank+1)
        self.img.size = (70,70)

        self.add_widget(self.img)

    def btn_press(self,x: int, y: int):
        print(f"btn {x} {y}")

class ChessBoard(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 8
        self.rows = 8
        self.padding = -1
        self.spacing = -2
        light_square = (242/255.0, 225/255.0, 195/255.0, 1)
        dark_square  = (195/255.0, 160/255.0, 130/255.0, 1)
        current_color = light_square

        self.cells = [] #stores all ui elements
        for line in range(8):
            self.cells.append([None, None, None, None, None, None, None, None])

        for rank in reversed(range(8)):
            for column in range(8):
                newCell = Cell(line,column,current_color,"./Assets/w_pawn.png")
                newCell.on_press = partial(self.selected, rank, column)
                self.cells[line][column] = newCell
                self.add_widget(newCell)
                
                if current_color == light_square:
                    current_color = dark_square
                else: 
                    current_color = light_square
            if current_color == light_square:
                    current_color = dark_square
            else: 
                current_color = light_square

    def selected(self, rank, column):
        print(f"selected {rank} {column}")

class ChessApp(App):
    pass

ChessApp().run()
