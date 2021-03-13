import sqlite3
from tkinter import *
from sqlite3 import *

def regis():
    global regis_screen
    regis_screen = Toplevel(main_screen)
    regis_screen.title("Register")
    regis_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(regis_screen, text="Please enter details below", bg='lightpink').pack()
    Label(regis_screen, text="").pack()
    username_label = Label(regis_screen, text="Username * ")
    username_label.pack()
    username_entry = Entry(regis_screen, textvariable=username)
    username_entry.pack()
    password_label = Label(regis_screen, text="Password * ")
    password_label.pack()
    password_entry = Entry(regis_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(regis_screen, text="").pack()
    Button(regis_screen,text="Register", width=10, height=1, bg='blue', command = regis_user).pack()

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command= login_verify).pack()

# def login_verify():
#     pass
#Pass this method 
def loginVerify():
    pass

def mainscreen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=regis).pack()
    
    main_screen.mainloop()

mainscreen()