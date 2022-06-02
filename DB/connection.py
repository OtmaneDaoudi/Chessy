# from msilib.schema import Error
import sqlite3

import UI.gameUI as ui

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
                cr.execute(
                    f"insert into users(username,psw) values('{username}','{psw}')")
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
        cr = db.cursor()
        if ui.GameUi.gameMode == 'PvP':
            cr.execute("update stats set total_played = total_played + 1 where mode = 'PVP'")
            db.commit()
            print("updated")
        else:
            cr.execute("update stats set total_played = total_played + 1 where mode = 'PVM'")
            db.commit()
            print("updated")

    def winner(color):
        cr = db.cursor()
        mode = "PVP" if ui.GameUi.gameMode == "PvP" else "PVM"
        if color == ui.GameUi.playAs:
            cr.execute(f"update stats set wins = wins + 1 where mode = '{mode}'")
        else:
            cr.execute(f"update stats set lost = lost + 1 where mode = '{mode}'")
        db.commit()

    def draw():
        cr = db.cursor()
        mode = "PVP" if ui.GameUi.gameMode == "PvP" else "PVM"
        cr.execute(f"update stats set draws = draws + 1 where mode = '{mode}'")
        db.commit()

    def update_score(newScore, score_time):
        cr = db.cursor()
        mode = "PVP" if ui.GameUi.gameMode == "PvP" else "PVM"
        cr.execute(f"update stats set best_score = {newScore}, best_score_time = {300-score_time} where mode = '{mode}' and best_score < {newScore}")
        print(f"score updated to {newScore} | time = {300-score_time}")
        db.commit()

    def update_best_time(newTime):
        cr = db.cursor()
        mode = "PVP" if ui.GameUi.gameMode == "PvP" else "PVM"
        cr.execute(f"update stats set best_time = {300-newTime} where mode = '{mode}' and (best_time > {300-newTime} or best_time=0)")
        print(f"best time updated to {300-newTime}")
        db.commit()
