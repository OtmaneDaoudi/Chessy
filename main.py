from kivymd.app import MDApp
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


class ChessApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        Connection.Connect() #initialise database connection
ChessApp().run() 