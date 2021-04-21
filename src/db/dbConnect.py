import sqlite3 as lite

def connect_sqLite():
    conn = lite.connect('db/iStock.db')
    return conn
