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
import UI.StatsScreen
from UI.gameUI import ChessBoard, GameUi
from kivy.uix.label import Label

class ContentPopChoice(BoxLayout):
    def __init__(self, pop, **kwargs):
        super().__init__(**kwargs)
        self.linkedPopUp = pop

    def anonymousInit(self):
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
        stored_data = JsonStore('data.json')
        if stored_data.exists('user1'):
            App.get_running_app().root.get_screen('home').ids.con.disabled = True
            App.get_running_app().root.get_screen('home').ids.dec.disabled = False
            App.get_running_app().root.get_screen('home').ids.stat.disabled = False
            App.get_running_app().root.get_screen('home').ids.con.opacity = '0'
            App.get_running_app().root.get_screen('home').ids.dec.opacity = '1'
        if os.path.exists("GameObject"):
            if os.path.getsize("GameObject") != 0: #file is not empty
                #show a pop up
                box = BoxLayout(orientation = "vertical")
                vbox = BoxLayout()
                lbl = Label(text="Voulez-vous charger la dernière partie sauvegardée?", size_hint = (1, 0.2), bold = True)
                vbox.add_widget(lbl)

                Boxed_layout= BoxLayout(orientation = "horizontal")
                btn1 = Button(text="Yes", size_hint=(1, .4), bold = True)
                btn2 = Button(text="no", size_hint=(1, .4) , bold = True)
                Boxed_layout.add_widget(btn1)
                Boxed_layout.add_widget(btn2)
        
                box.add_widget(vbox)
                box.add_widget(Boxed_layout)

                pop = Popup(title="Chargement du jeu précédent",content=box, size_hint=(None, None), size=(400, 300))
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
        window = Popup(title="Joueur VS. Joueur", size_hint=(None, None), size=(300, 300))
        show = ContentPopChoice(window)
        window.content = show
        window.open()
        return True

    def init_stats_screen(self):
        App.get_running_app().root.add_widget(UI.StatsScreen.StatsScreen())
        # App.get_running_app().root.get_screen('stats').fetch_stats()