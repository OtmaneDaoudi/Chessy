from ctypes.wintypes import RGB
from turtle import color
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from Classes.Board import Board
from Classes.Game import Game
from kivy.app import App
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.button import Button
from functools import partial

Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'resizable', False)


# game = Game()
# game.start_game()

# i = [1,2,""]
# p = list(map(type, i)).count(int)
# print(p)

class Cell(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
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
        for line in reversed(range(8)):
            for column in range(8):
                btn = Button(background_normal='./Assets/temp/b5.png',background_color=current_color)
                btn.on_press = partial(self.btn_press, line, column)
                self.add_widget(btn)
                if current_color == light_square:
                    current_color = dark_square
                else: 
                    current_color = light_square
            if current_color == light_square:
                    current_color = dark_square
            else: 
                current_color = light_square

    def btn_press(self,x: int, y: int):
        print(f"btn {x} {y}")



class ChessApp(App):
    pass


ChessApp().run()
