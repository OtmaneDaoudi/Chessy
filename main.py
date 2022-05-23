from kivy.app import App
from UI.gameUI import *
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import BooleanProperty
from kivy.config import Config

class ChessApp(App):
    pass


class WindowManager(ScreenManager):
    pass


class HomePage(Screen):
    pass

    # +--------- Player VS Player Screen ---------+

class PvspScreen(Screen):
    color_clicked = BooleanProperty(True)

    def on_color_button_click(self, widget):

        if widget.state == "down":
            if self.color_clicked == False:
                self.color_clicked = True
            else:
                self.color_clicked = False

    # +--------- Player VS Machine Screen ---------+
    
class PvsmScreen(Screen):
    color_clicked = BooleanProperty(True)
    level_clicked1 = BooleanProperty(True)
    level_clicked2 = BooleanProperty(False)
    level_clicked3 = BooleanProperty(False)

    def on_color_button_click(self, widget):

        if widget.state == "down":
            if self.color_clicked == False:
                self.color_clicked = True
            else:
                self.color_clicked = False

    def on_level_button_click(self, widget, id):
        if widget.state == "down":
            if id == 1:
                if self.level_clicked1 == False:
                    self.level_clicked1 = True
                    self.level_clicked2 = False
                    self.level_clicked3 = False
                else:
                    self.level_clicked1 = False
                    self.level_clicked2 = True
                    self.level_clicked3 = True
            elif id == 2:
                if self.level_clicked2 == False:
                    self.level_clicked2 = True
                    self.level_clicked1 = False
                    self.level_clicked3 = False
                else:
                    self.level_clicked2 = False
                    self.level_clicked1 = True
                    self.level_clicked3 = True
            else:
                if self.level_clicked3 == False:
                    self.level_clicked3 = True
                    self.level_clicked1 = False
                    self.level_clicked2 = False
                else:
                    self.level_clicked3 = False
                    self.level_clicked1 = True
                    self.level_clicked2 = True


ChessApp().run()

# class ChessApp(App):
#     pass

# if __name__ == '__main__':
#     ChessApp().run()
#     print("out UI")
#     print("running threads , ", threading.enumerate())