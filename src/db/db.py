import sqlite3
import time
import datetime
import random

conn = sqlite3.connect("db/istock.db")

def create_table():
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot (unix REAL, datestamp TEXT, keyword TEXT, value REAL)')
    c.close()

def data_entry():
    c = conn.cursor()
    c.execute("INSERT INTO stuffToPlot VALUES (145123542, '2016-01-03', 'Python', 7)")
    conn.commit()
    c.close()


create_table()
data_entry()