from functools import partial
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import  Screen
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
import pickle
import os
from kivy.storage.jsonstore import JsonStore
from UI.gameUI import ChessBoard, GameUi

class ContentPopChoice(BoxLayout):
    def __init__(self, pop, **kwargs):
        super().__init__(**kwargs)
        self.linkedPopUp = pop

    def anonymousInit(self):
        print("anony pressed")
        self.linkedPopUp.dismiss()
        App.get_running_app().root.current = 'pvsp'
    
    def loginInit(self):
        GameUi.authType = "Auth"
        self.linkedPopUp.dismiss()
        App.get_running_app().root.current = 'connect'

class HomePage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.showSavedGameDialogue)
    # +--------- Player VS Player Screen ---------+

    def showSavedGameDialogue(self, *args):
        if os.path.exists("GameObject"):
            if os.path.getsize("GameObject") != 0: #file is not empty
                #show a pop up
                btn1 = Button(text="Yes", size_hint=(1, None), height = 80)
                btn2 = Button(text="no", size_hint=(1, None), height = 80)
                Boxed_layout= BoxLayout(orientation = "horizontal")
                Boxed_layout.add_widget(btn1)
                Boxed_layout.add_widget(btn2)
                pop = Popup(title="Do you want to load the last saved game?",content=Boxed_layout, size_hint=(.9,.3))
                btn1.bind(on_release=partial(self.loadSavedGame, pop))
                # btn1.bind(on_release=partial(doit, pop)) # bind to whatever action is being confiirmed
                btn2.bind(on_release=pop.dismiss)
                pop.open()
                
    def loadSavedGame(self, pop, *args):
        print("loading saved game")
        game_instance = None
        with open('GameObject','rb') as f:
                 game_instance = pickle.load(f) #serialised game instance
        #clear file
        to_clear = open("GameObject","w")
        to_clear.close()
        ChessBoard.loaded_game = game_instance
        pop.dismiss()
        gameui = GameUi()
        GameUi.current_gameui = gameui
        gameui.name = 'gameUi'
        gameui.id = 'gameUi'
        App.get_running_app().root.add_widget(gameui)
        App.get_running_app().root.current = 'gameUi'

    def deconnexion(self):
        stored_data = JsonStore('data.json')
        stored_data.delete('user1')
        if stored_data.exists('user2'):
            stored_data.delete('user2')
            # self.parent.current = "home"
        App.get_running_app().root.get_screen('home').ids.con.disabled = False
        App.get_running_app().root.get_screen('home').ids.dec.disabled = True
        App.get_running_app().root.get_screen('home').ids.stat.disabled = True
        App.get_running_app().root.get_screen('home').ids.con.opacity = '1'
        App.get_running_app().root.get_screen('home').ids.dec.opacity = '0'

    def playerVsPlayerInit(self, *args):
        if os.path.getsize("data.json") == 2: #empty JSON file
            App.get_running_app().root.current = 'pvsp'
        else:
            self.show_choice_pop(); 

    def show_choice_pop(self):
        window = Popup(title="Player VS Player", size_hint=(None, None), size=(300, 300))
        show = ContentPopChoice(window)
        window.content = show
        window.open()
        return True