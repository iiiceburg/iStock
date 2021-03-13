import sqlite3 as lite
from sqlite3 import Error
from tkinter import *

def connect(db):
    try:
        conn = lite.connect(db)
        return conn
    except Error as e:
        print(e)
    finally:
        conn.close()


