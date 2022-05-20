from kivy.app import App
from UI.gameUI import *


class ChessApp(App):
    pass

if __name__ == '__main__':
    ChessApp().run()
    
#close all active Ai threads
# for thread in threading.enumerate():
#     if thread.name == "AI":
#         print("AI thread running , killing...")
#         threading.