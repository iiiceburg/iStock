import sqlite3 as lite


# dbPath = "db/iStock.db"

def connect_sqLite():
    conn = lite.connect('db/iStock.db')
    return conn



# class loginCheck():
#     def check():
        
# def data_entry():
#     c = conn.cursor()
#     c.execute('INSERT INTO users (username,password,name,email,phone,timestamp) VALUES ("horizon","peeranat123","Peeranat Ounhanan","ounhanan2015@gmail.com","0616454483",timeStamp);')
#     conn.commit()
#     c.close()

# data_entry()
