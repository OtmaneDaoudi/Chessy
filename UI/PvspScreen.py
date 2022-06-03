from kivy.uix.screenmanager import  Screen
from kivy.properties import BooleanProperty
from kivy.properties import BooleanProperty

from UI.gameUI import GameUi

class PvspScreen(Screen):
    color_clicked = BooleanProperty(True)

    def on_color_button_click(self, widget):
        if widget.text == "Black":
            print("play as black")
            GameUi.playAs = "b"
        else:
            print("play as white")
            GameUi.playAs = "w"
        if widget.state == "down":
            if self.color_clicked == False:
                self.color_clicked = True
            else:
                self.color_clicked = False
    
    def init_game(self):
        #player versus machine
        #get UI data 
        
        GameUi.gameMode = "PvP"
        gameui = GameUi()
        GameUi.current_gameui = gameui
        gameui.name = 'gameUi'
        gameui.id = 'gameUi'
        self.parent.add_widget(gameui)
        self.parent.current = 'gameUi'