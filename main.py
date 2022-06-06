from kivy.app import App
from UI.HomePage import HomePage
from UI.PvspScreen import PvspScreen
from UI.PvsmScreen import PvsmScreen
from UI.gameUI import *
from DB.connection import Connection
from UI.StatsScreen import StatsScreen
from UI.ConnectionPg import ConnectionPg
from kivy.config import Config

Config.set('graphics', 'width', '830')
Config.set('graphics', 'height', '720')
Config.set('graphics', 'resizable', True)
Config.set('kivy', 'keyboard_mode', 'system')
# Window.borderless = True
Config.write()


class ChessApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Connection.Connect() #initialise database connection
ChessApp().run() 