from kivy.app import App
from UI.gameUI import *
from DB.connection import Connection

class ChessApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Connection.Connect() #initialise database connection
ChessApp().run()