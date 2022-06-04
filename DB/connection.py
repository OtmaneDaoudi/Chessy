# from msilib.schema import Error
import sqlite3

import UI.gameUI as ui
from kivy.storage.jsonstore import JsonStore

class Connection():
    def Connect():
        try:
            global db
            db = sqlite3.connect("./DB/chessdb.db")
            print("Connected To Database Successfully")
        except sqlite3.Error as er:
            print(er)
        return db

    @staticmethod
    def check_user(username):
        try:
            cr = db.cursor()
            cr.execute(f"select * from users where username='{username}'")
            row = cr.fetchone()
            if(row is None):
                return False
            return True
        except sqlite3.Error as er:
            print(er)
    
    @staticmethod
    def get_user(username,psw):
        try:
            cr = db.cursor()
            cr.execute(f"select * from users where username='{username}' and psw='{psw}'")
            return cr.fetchone()
        except sqlite3.Error as er:
            print(er)


    def add_user(username, psw):
        try:
            if(not Connection.check_user(username)):
                cr = db.cursor()
                cr.execute(f"insert into users(username,psw) values('{username}','{psw}')")
                cr.execute(f"select id from users where username = '{username}' and psw = '{psw}'")
                user = cr.fetchone(); 
                print("user = ", user)
                cr.execute(f"insert into stats values (NULL, 0, 0, 0, 'PvP', 0, 0, 0, 0, {user[0]})")
                cr.execute(f"insert into stats values (NULL, 0, 0, 0, 'PvM', 0, 0, 0, 0, {user[0]})")
                db.commit()
                print("------------User Is Inserted-----------")
                return True
            else:
                print("------------User Exists -----------")
                return False
        except sqlite3.Error as er:
            print(er)

    def getStats():
        # try:
        #     cr = db.cursor()
        #     cr.execute("select * from stats")
        #     return cr.fetchall()
        # except sqlite3.Error as er:
        #     print(er) 
        pass

    def increment_total_played(*args):
        stored_data = JsonStore('data.json')
        cr = db.cursor()
        if ui.GameUi.gameMode == 'PvM':
            cr.execute(f"update stats set total_played = total_played + 1 where mode = 'PvM' and user = {stored_data.get('user1')['id']}")
        else:
            if ui.GameUi.authType != "Anonymous":
                cr.execute(f"update stats set total_played = total_played + 1 where mode = 'PvP' and user = {stored_data.get('user1')['id']}")
                cr.execute(f"update stats set total_played = total_played + 1 where mode = 'PvP' and user = {stored_data.get('user2')['id']}")
        print("total played updated")
        db.commit()

    def winner(color):
        cr = db.cursor()
        stored_data = JsonStore('data.json')
        if ui.GameUi.gameMode == "PvP" and ui.GameUi.authType == "Auth":
            if color == ui.GameUi.playAs:
                cr.execute(f"update stats set wins = wins + 1 where mode = 'PvP' and user = {stored_data.get('user1')['id']}")
                cr.execute(f"update stats set lost = lost + 1 where mode = 'PvP' and user = {stored_data.get('user2')['id']}")
            else:
                cr.execute(f"update stats set lost = lost + 1 where mode = 'PvP' and user = {stored_data.get('user1')['id']}")
                cr.execute(f"update stats set wins = wins + 1 where mode = 'PvP' and user = {stored_data.get('user2')['id']}")
        elif ui.GameUi.gameMode == 'PvM' and stored_data.exists('user1'):
            if color == ui.GameUi.playAs:
                cr.execute(f"update stats set wins = wins + 1 where mode = 'PvM' and user = {stored_data.get('user1')['id']}")
            else:   
                cr.execute(f"update stats set lost = lost + 1 where mode = 'PvM' and user = {stored_data.get('user1')['id']}")
        db.commit()

    def draw():
        cr = db.cursor()
        stored_data = JsonStore('data.json')
        if ui.GameUi.gameMode == "PvP" and ui.GameUi.authType == "Auth":
            cr.execute(f"update stats set draws = draws + 1 where mode = 'PvP' and user IN ({stored_data.get('user1')['id']},{stored_data.get('user2')['id']})")
        elif ui.GameUi.gameMode == 'PvM' and stored_data.exists('user1'):
            cr.execute(f"update stats set draws = draws + 1 where mode = 'PvM' and user = {stored_data.get('user1')['id']}")
        db.commit()

    def update_score(newScore, score_time):
        # cr = db.cursor()
        # mode = "PVP" if ui.GameUi.gameMode == "PvP" else "PVM"
        # cr.execute(f"update stats set best_score = {newScore}, best_score_time = {300-score_time} where mode = '{mode}' and best_score < {newScore}")
        # print(f"score updated to {newScore} | time = {300-score_time}")
        # db.commit()
        pass

    def update_best_time(newTime):
        # cr = db.cursor()
        # mode = "PVP" if ui.GameUi.gameMode == "PvP" else "PVM"
        # cr.execute(f"update stats set best_time = {300-newTime} where mode = '{mode}' and (best_time > {300-newTime} or best_time=0)")
        # print(f"best time updated to {300-newTime}")
        # db.commit()
        pass
