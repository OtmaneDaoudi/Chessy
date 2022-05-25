from kivy.uix.screenmanager import  Screen
from kivy.properties import BooleanProperty
from kivy.properties import BooleanProperty

from UI.gameUI import GameUi

class PvsmScreen(Screen):
    color_clicked = BooleanProperty(True)
    level_clicked1 = BooleanProperty(True)
    level_clicked2 = BooleanProperty(False)
    level_clicked3 = BooleanProperty(False)

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

    def on_level_button_click(self, widget, id):
        if widget.state == "down":
            if id == 1:
                GameUi.diff = 1
                print("diff updated to 1")
                if self.level_clicked1 == False:
                    self.level_clicked1 = True
                    self.level_clicked2 = False
                    self.level_clicked3 = False
                else:
                    self.level_clicked1 = False
                    self.level_clicked2 = True
                    self.level_clicked3 = True
            elif id == 2:
                GameUi.diff = 2
                print("diff updated to 2")
                if self.level_clicked2 == False:
                    self.level_clicked2 = True
                    self.level_clicked1 = False
                    self.level_clicked3 = False
                else:
                    self.level_clicked2 = False
                    self.level_clicked1 = True
                    self.level_clicked3 = True
            else:
                GameUi.diff = 3
                print("diff updated to 3")
                if self.level_clicked3 == False:
                    self.level_clicked3 = True
                    self.level_clicked1 = False
                    self.level_clicked2 = False
                else:
                    self.level_clicked3 = False
                    self.level_clicked1 = True
                    self.level_clicked2 = True

    def init_game(self, *args):
        #player versus machine
        #get UI data 
        
        GameUi.gameMode = "PvM"

        gameui = GameUi()
        GameUi.current_gameui = gameui
        print("done initialising")
        gameui.name = 'gameUi'
        gameui.id = 'gameUi'
        self.parent.add_widget(gameui)
        self.parent.current = 'gameUi'
    #     Clock.schedule_once(self.setCurrent, .2)

    # def setCurrent(self, *args):
    #     self.parent.current = 'gameUi'

    #============================================
