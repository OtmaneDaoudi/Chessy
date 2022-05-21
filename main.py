from kivy.app import App
from UI.gameUI import *
import sys
import threading 

class ChessApp(App):
    pass

if __name__ == '__main__':
    ChessApp().run()
    print("out UI")
    print("running threads , ", threading.enumerate())