from kivy.app import App
from kivy.uix.screenmanager import Screen
from DB.connection import Connection
from kivy.storage.jsonstore import JsonStore

from UI.gameUI import GameUi

class ConnectionPg(Screen): 
    def __init__(self, **kwargs):
            super().__init__(**kwargs)

    def signUp(self):
        username = self.username.text.strip()
        psw = self.psw.text.strip()
        self.username.text = ''
        self.psw.text = ''
        if(username != '' and psw != ''):
            if(Connection.add_user(username, psw)):
                obj = Connection.get_user(username, psw)
                if(obj is not None):
                    stored_data = JsonStore('data.json')
                    if stored_data.exists('user1'):
                        stored_data.put('user2', id=obj[0], userName = obj[1])
                        self.parent.current = "pvsp"
                        return
                    else:   
                        stored_data.put('user1', id=obj[0], userName = obj[1])
                    App.get_running_app().root.get_screen('home').ids.con.disabled = True
                    App.get_running_app().root.get_screen('home').ids.dec.disabled = False
                    App.get_running_app().root.get_screen('home').ids.stat.disabled = False
                    App.get_running_app().root.get_screen('home').ids.con.opacity = '0'
                    App.get_running_app().root.get_screen('home').ids.dec.opacity = '1'
                    App.get_running_app().root.get_screen('connect').ids.noti.text = ''
                    self.parent.current = "home"
            else:
                App.get_running_app().root.get_screen('connect').ids.noti.text = "l'utilisateur existe déjà!"

    def signIn(self):
        username = self.username.text.strip()
        psw = self.psw.text.strip()
        self.username.text = ''
        self.psw.text = ''
        if(username != '' and psw != ''):
            obj = Connection.get_user(username, psw)
            print(obj)
            if(obj is not None):
                stored_data = JsonStore('data.json')
                if stored_data.exists('user1'):
                    #consider current player as second one
                    if stored_data.get('user1')['id'] == obj[0]:
                        App.get_running_app().root.get_screen('connect').ids.noti.text = 'Premier utilisateur déjà connecté'
                        return
                    else:
                        stored_data.put('user2', id=obj[0], userName = obj[1])
                        self.parent.current = "pvsp"
                        return
                else:
                    stored_data.put('user1', id=obj[0], userName = obj[1])
                App.get_running_app().root.get_screen('home').ids.con.disabled = True
                App.get_running_app().root.get_screen('home').ids.dec.disabled = False
                App.get_running_app().root.get_screen('home').ids.stat.disabled = False
                App.get_running_app().root.get_screen('home').ids.con.opacity = '0'
                App.get_running_app().root.get_screen('home').ids.dec.opacity = '1'
                App.get_running_app().root.get_screen('connect').ids.noti.text = ''
                self.parent.current = "home"
            else:
                App.get_running_app().root.get_screen('connect').ids.noti.text = "Le nom d'utilisateur ou le mot de passe est invalide !"



    def fix(self):
        print("fixed")
        GameUi.authType = "Anonymous"