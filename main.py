from kivy.app import App
from UI.gameUI import *

class ChessApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Connection.Connect()
        # try:
        #     with open('GameObject','rb') as f:
        #         obj = pickle.load(f)
        #     print(obj)
        # except FileNotFoundError:
        #      print("The 'doc' directory does not exist")

# ChessApp().run()

obj = None
db = Connection.Connect()
try:
    with open('GameObject','rb') as f:
        obj = pickle.load(f)
except FileNotFoundError:
     print("The 'doc' directory does not exist")

obj.game_board.printBoard()