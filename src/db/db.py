import sqlite3 as lite
from sqlite3 import Error
from tkinter import *

con = lite.connect("db/istock.db")
curs = con.cursor()
con.commit()
con.close()


