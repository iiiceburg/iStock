from tkinter import * 
import os, sys
import sqlite3
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# import ../db/dbConnect.py
from db.dbConnect import connect_sqLite

class MainAuthen():
    def window():
        mainWindow = Tk()
        mainWindow.geometry("900x600+500+150")
        mainWindow.title("Istock")
        mainWindow.configure(bg="white")
        mainWindow.rowconfigure((0,1),weight = 1)
        mainWindow.columnconfigure((0,2),weight = 1)
        mainWindow.resizable(0,0)
        return mainWindow
        
    global combine_funcs_login
    def combine_funcs_login(mainWindow):
        loginScreen()
        mainWindow.destroy()
    
    global combine_funcs_register
    def combine_funcs_register(mainWindow):
        registerScreen()
        mainWindow.destroy()

    #When user click register but user already have account , user must click button which register screen have to close and login screen open
    global combine_funcs_already_acc 
    def combine_funcs_already_acc(reg_screen):
        loginScreen()
        reg_screen.destroy()        

    global combine_funcs_no_acc
    def combine_funcs_no_acc(login_screen):
        registerScreen()
        login_screen.destroy()    

    def auth_main_screen(mainWindow):
        Label(mainWindow,text="Welcome to iStock",fg="black",bg="white",font="vandara 22 bold").grid(row=0,column=1,sticky=N,pady=(100,0))
        Label(mainWindow,text="Stock management system",fg="black",bg="white",font="vandara 10").grid(row=0,column=1,sticky=N,pady=(150,0))
        Button(mainWindow,text="Login",fg="black",bg="orange",font = "vandara 16 bold",width=20,height=2,command=lambda:combine_funcs_login(mainWindow)).grid(row=0,column=1,pady=(50,0))
        Button(mainWindow,text="Register",fg="orange",bg="#333333",font = "vandara 16 bold",width=20,height=2,command=lambda:combine_funcs_register(mainWindow)).grid(row=0,column=1,pady=(200,0))
    
    global loginScreen

    def loginScreen():
        login_screen = Tk()
        login_screen.geometry("900x600+500+150")
        login_screen.title("iStock")
        login_screen.configure(bg="white")
        login_screen.rowconfigure((0,1),weight = 1)
        login_screen.columnconfigure((0,2),weight = 1)
        login_screen.resizable(0,0)

        login_username = StringVar()
        login_password = StringVar()

        Label(login_screen,text="LOGIN",fg="black",bg="white",font="vandara 22 bold").grid(row=0,column=1,sticky=N,pady=(100,0))
        Label(login_screen,text="Please login to your account",fg="black",bg="white",font="vandara 10").grid(row=0,column=1,sticky=N,pady=(150,0))
        Label(login_screen,text="Username",fg="black",bg="white",font="vandara 10").place(x=325,y=180)
        Label(login_screen,text="Password",fg="black",bg="white",font="vandara 10").place(x=325,y=255)
        Entry(login_screen,textvariable =  login_username,width=20,bg="lightgrey",fg="black",font="vandara 16 bold",relief='flat',justify=CENTER).grid(row=0,column=1,pady=(50,0),ipady=10)
        Entry(login_screen,textvariable=  login_password,show= '*',width=20,bg="lightgrey",fg="black",font="vandara 16 bold",relief='flat',justify=CENTER).grid(row=0,column=1,pady=(200,0),ipady=10,)
        Button(login_screen,text="Login",fg="black",bg="orange",font = "vandara 12 bold",width=14,height=2).grid(row=0,column=1,pady=(50,0),sticky=S)
        Button(login_screen,text="Don't have an account yet? Register",fg="black",bg="white",font = "vandara 10 bold",relief=FLAT,height=2,command=lambda:combine_funcs_no_acc(login_screen)).grid(row=1,column=1,sticky=N,pady=(10,0))

#"Don't have an account yet?  Sign Up
    global registerScreen
    def registerScreen():
        reg_screen = Tk()
        reg_screen.geometry("900x600+500+150")
        reg_screen.title("iStock")
        reg_screen.configure(bg="white")
        reg_screen.rowconfigure((0,3),weight = 1)
        reg_screen.columnconfigure((0,2),weight = 1)
        reg_screen.resizable(0,0)  
        global reg_username , reg_password , reg_name , reg_email , reg_phone
        global username_entry , pass_entry , name_entry , email_entry , phone_entry
        reg_username = StringVar()
        reg_password = StringVar()
        reg_name = StringVar()
        reg_email = StringVar()
        reg_phone = StringVar()
        Label(reg_screen,text="CREATE ACCOUNT",fg="black",bg="white",font="vandara 22 bold").grid(row=0,column=1,sticky=N,pady=(50,0))
        Label(reg_screen,text="Username",fg="black",bg="white",font="vandara 10").place(x=325,y=100)
        Label(reg_screen,text="Password",fg="black",bg="white",font="vandara 10").place(x=325,y=170)
        Label(reg_screen,text="Name",fg="black",bg="white",font="vandara 10").place(x=325,y=240)
        Label(reg_screen,text="Email",fg="black",bg="white",font="vandara 10").place(x=325,y=310)
        Label(reg_screen,text="Phone",fg="black",bg="white",font="vandara 10").place(x=325,y=380)
        username_entry = Entry(reg_screen,width=20, textvariable = reg_username,bg="lightgrey",fg="black",font="vandara 16 bold",relief='flat',justify=CENTER)
        username_entry.grid(row=0,column=1,pady=(120,0),ipady=10,sticky=N)
        pass_entry = Entry(reg_screen,width=20, textvariable = reg_password,bg="lightgrey",fg="black",font="vandara 16 bold",relief='flat',justify=CENTER)
        pass_entry.grid(row=0,column=1,pady=(190,0),ipady=10,sticky=N)
        name_entry = Entry(reg_screen,width=20, textvariable = reg_name,bg="lightgrey",fg="black",font="vandara 16 bold",relief='flat',justify=CENTER)
        name_entry.grid(row=0,column=1,pady=(260,0),ipady=10,sticky=N)
        email_entry = Entry(reg_screen,width=20, textvariable = reg_email,bg="lightgrey",fg="black",font="vandara 16 bold",relief='flat',justify=CENTER)
        email_entry.grid(row=0,column=1,pady=(330,0),ipady=10,sticky=N)
        phone_entry = Entry(reg_screen,width=20, textvariable = reg_phone,bg="lightgrey",fg="black",font="vandara 16 bold",relief='flat',justify=CENTER)
        phone_entry.grid(row=0,column=1,pady=(400,0),ipady=10,sticky=N)
        Button(reg_screen,text="Register",fg="black",bg="orange",font = "vandara 12 bold",width=14,height=2,command=register_insert_data).grid(row=0,column=1,pady=(470,0))
        Button(reg_screen,text="Already have an account? Login",fg="black",bg="white",font = "vandara 10 bold",relief=FLAT,height=2,command=lambda:combine_funcs_already_acc(reg_screen)).grid(row=1,column=1)
        

    global register_insert_data
    def register_insert_data():
        
        get_username = username_entry.get()
        get_password = pass_entry.get()
        get_name = name_entry.get()
        get_email = email_entry.get()
        get_phone = phone_entry.get()     

        conn = sqlite3.connect('src\db\istock.db')
        curs = conn.cursor()
        reg_insert_data = """INSERT INTO users(username,password,name,email,phone) 
        VALUES(?,?,?,?,?);"""
        curs.execute(reg_insert_data,(get_username,get_password,get_name,get_email,get_phone))
        conn.commit()
        curs.close()
    
        print(reg_insert_data)

        print("Username : ",get_username)
        print("Password : %s"%get_password)
        print("Name : ",name_entry.get())
        print("Email : ",get_email)
        print("Phone : ",get_phone)


    mainWindow = window()
    
    auth_main_screen(mainWindow)
    mainWindow.mainloop()


        
    






