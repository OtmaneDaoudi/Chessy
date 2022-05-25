from msilib.schema import Error
from random import getstate
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

    def getStats():
        try:
            cr = db.cursor()
            cr.execute("select * from stats")
            return cr.fetchall()
        except sqlite3.Error as er:
            print(er)