import sqlite3 as lite

import time
import datetime
import random

dbPath = "db/iStock.db"
conn = lite.connect("db/iStock.db")
timeStamp = datetime.datetime.now()


def data_entry():
    c = conn.cursor()
    c.execute('INSERT INTO users (username,password,name,email,phone,timestamp) VALUES ("horizon","peeranat123","Peeranat Ounhanan","ounhanan2015@gmail.com","0616454483",timeStamp);')
    conn.commit()
    c.close()

data_entry()
print("Insert success")
