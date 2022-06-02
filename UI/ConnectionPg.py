from kivy.app import App
from kivy.uix.screenmanager import Screen
from DB.connection import Connection
from kivy.storage.jsonstore import JsonStore

class ConnectionPg(Screen): 
    def __init__(self, **kwargs):
            super().__init__(**kwargs)
        # @classmethod

    def signUp(self):
        username = self.username.text.strip()
        psw = self.psw.text.strip()
        self.username.text = ''
        self.psw.text = ''
        if(username != '' and psw != ''):
            if(Connection.add_user(username, psw)):
                App.get_running_app().root.get_screen('home').ids.con.disabled = True
                App.get_running_app().root.get_screen('home').ids.dec.disabled = False
                App.get_running_app().root.get_screen('home').ids.stat.disabled = False
                App.get_running_app().root.get_screen('home').ids.con.opacity = '0'
                App.get_running_app().root.get_screen('home').ids.dec.opacity = '1'
                App.get_running_app().root.get_screen('connect').ids.noti.text = ''
                self.parent.current = "home"
            else:
                App.get_running_app().root.get_screen(
                    'connect').ids.noti.text = 'The username is existed !'
    def signIn(self):
        username = self.username.text.strip()
        psw = self.psw.text.strip()
        self.username.text = ''
        self.psw.text = ''
        if(username != '' and psw != ''):
            obj = Connection.get_user(username, psw)
            if(obj is not None):
                stored_data = JsonStore('data.json')
                stored_data.put('user', myobjet=obj)
                App.get_running_app().root.get_screen('home').ids.con.disabled = True
                App.get_running_app().root.get_screen('home').ids.dec.disabled = False
                App.get_running_app().root.get_screen('home').ids.stat.disabled = False
                App.get_running_app().root.get_screen('home').ids.con.opacity = '0'
                App.get_running_app().root.get_screen('home').ids.dec.opacity = '1'
                App.get_running_app().root.get_screen('connect').ids.noti.text = ''
                self.parent.current = "home"
            else:
                App.get_running_app().root.get_screen(
                    'connect').ids.noti.text = 'The username or password is invalid !'