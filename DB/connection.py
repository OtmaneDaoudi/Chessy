from msilib.schema import Error
import sqlite3

class Connection():
    def Connect():
        try:
            global db
            db = sqlite3.connect("DB/chessdb.db")
            print("Connected To Database Successfully")
        except sqlite3.Error as er:
            print(er)
        return db


    def getPath():
        try:
            cr = db.cursor()
            cr.execute("select path from saved_game")
            return cr.fetchone()[0]
        except sqlite3.Error as er:
            print(er)

    def setPath(path):
        try:
            cr = db.cursor()
            cr.execute("delete from saved_game")
            cr.execute(f"insert into saved_game(path) values('{path}')")
            db.commit()
            print("------------Inserted-----------")    
        except sqlite3.Error as er:
            print(er)
        return True

    def getStats():
        try:
            cr = db.cursor()
            cr.execute("select * from stats")
            return cr.fetchall()
        except sqlite3.Error as er:
            print(er)