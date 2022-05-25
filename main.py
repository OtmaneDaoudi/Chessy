from kivy.app import App
from UI.HomePage import HomePage
from UI.PvspScreen import PvspScreen
from UI.PvsmScreen import PvsmScreen
from UI.gameUI import *
from DB.connection import Connection
from UI.StatsScreen import StatsScreen
class ChessApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Connection.Connect() #initialise database connection
ChessApp().run()