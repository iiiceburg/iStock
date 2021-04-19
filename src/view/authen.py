import os, sys
import hashlib
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sqlite3 import Error
import tkinter as tk
from tkinter.constants import *
from tkinter import messagebox
import sqlite3 as lite
from view.home import Home

#Mainclass
class MainAuthen(tk.Frame):
    def __init__(self, root):
        self.root = root
        tk.Frame.__init__(self, self.root)
        self.reg_username = tk.StringVar()
        self.reg_password = tk.StringVar()
        self.reg_conpass = tk.StringVar()
        self.reg_name = tk.StringVar()
        self.reg_email = tk.StringVar()
        self.reg_phone = tk.StringVar()
        self.welcome()
    
    #Welcome page display Login and Register button
    def welcome(self):
        self.root.geometry("900x600+500+150")
        self.root.title("Istock")
        self.root.configure(bg="white")
        self.root.rowconfigure((0,1),weight = 1)
        self.root.columnconfigure((0,2),weight = 1)
        self.root.resizable(0,0)
        self.lbl1 = tk.Label(self.root,text="Welcome to iStock",fg="black",bg="white",font="vandara 22 bold")
        self.lbl1.grid(row=0,column=1,sticky=N,pady=(100,0))
        self.lbl2 = tk.Label(self.root,text="Stock management system",fg="black",bg="white",font="vandara 10")
        self.lbl2.grid(row=0,column=1,sticky=N,pady=(150,0))
        self.btn1 = tk.Button(self.root,text="Login",fg="black",bg="orange",font = "vandara 16 bold",width=20,height=2,command=lambda:[self.root.destroy(),self.loginScreen(tk.Tk())])
        self.btn1.grid(row=0,column=1,pady=(50,0))
        self.btn2 = tk.Button(self.root,text="Register",fg="orange",bg="#333333",font = "vandara 16 bold",width=20,height=2,command=lambda:[self.root.destroy(),self.registerScreen(tk.Tk())])
        self.btn2.grid(row=0,column=1,pady=(200,0))

    #Login form user login into Program which if user don't have account , user can click btn to register page
    def loginScreen(self,login):
        self.login = login
        self.login.geometry("900x600+500+150")
        self.login.title("Login")
        self.login.configure(bg="white")
        self.login.rowconfigure((0,1),weight = 1)
        self.login.columnconfigure((0,2),weight = 1)
        self.login.resizable(0,0)
        self.login_username = tk.StringVar()
        self.login_password = tk.StringVar()
        self.loginlbl1 = tk.Label(self.login,text="LOGIN",fg="black",bg="white",font="vandara 22 bold")
        self.loginlbl1.grid(row=0,column=1,sticky=N,pady=(100,0))
        self.loginlbl2 = tk.Label(self.login,text="Please login to your account",fg="black",bg="white",font="vandara 10")   
        self.loginlbl2.grid(row=0,column=1,sticky=N,pady=(150,0))
        self.loginlbl3 = tk.Label(self.login,text="Username",fg="black",bg="white",font="vandara 10")
        self.loginlbl3.place(x=325,y=180)
        self.loginlbl4 = tk.Label(self.login,text="Password",fg="black",bg="white",font="vandara 10")
        self.loginlbl4.place(x=325,y=255)
        self.loginlbl5 = tk.Entry(self.login,width=20,bg="lightgrey",textvariable=self.login_username,fg="black",font="vandara 16 bold",relief='flat',justify=CENTER)
        self.loginlbl5.grid(row=0,column=1,pady=(50,0),ipady=10)
        self.loginlbl6 = tk.Entry(self.login,textvariable=self.login_password,show= '*',width=20,bg="lightgrey",fg="black",font="vandara 16 bold",relief='flat',justify=CENTER)
        self.loginlbl6.grid(row=0,column=1,pady=(200,0),ipady=10)
        self.login_btn = tk.Button(self.login,text="Login",fg="black",bg="orange",font = "vandara 12 bold",width=14,height=2,command=lambda:LoginCheck.searchData(self.login_username.get(),self.login_password.get()))
        self.login_btn.grid(row=0,column=1,pady=(50,0),sticky=S)
        self.to_reg = tk.Button(self.login,text="Don't have an account yet? Register",fg="black",bg="white",command=lambda:[self.login.destroy(),self.registerScreen(tk.Tk())],font = "vandara 10 bold",relief=FLAT,height=2)
        self.to_reg.grid(row=1,column=1,sticky=N,pady=(10,0))
    
    #Regsitration form for new user which user already account can click button for redirect to login page
    def registerScreen(self,reg_screen):
        self.reg_screen = reg_screen
        self.reg_screen.geometry("900x600+500+150")
        self.reg_screen.title("Registration")
        self.reg_screen.configure(bg="white")
        self.reg_screen.rowconfigure((0,3),weight = 1)
        self.reg_screen.columnconfigure((0,2),weight = 1)
        self.reg_screen.resizable(0,0)  
        self.lblreg_list = ["Username","Password","Confirm Password","Name","Email","Phone"]
        self.reg_val_list = [self.reg_username , self.reg_password , self.reg_conpass , self.reg_name , self.reg_email , self.reg_phone ]
        reg_data = []
        for i,items in enumerate(self.lblreg_list):
            self.a = tk.Label(reg_screen,text=items,fg="black",bg="white",font="vandara 10")
            self.a.place(x=325,y=((i*70)+45))
            self.reg_entry = tk.Entry(reg_screen,width=20, textvariable =self.reg_val_list[i],bg="lightgrey",fg="black",font="vandara 16 bold",relief='flat',justify=CENTER)
            self.reg_entry.grid(row=0,column=1,pady=(((i*70)+65),0),ipady=10,sticky=N)
            reg_data.append(self.reg_entry)
        self.reg_btn1 = tk.Button(reg_screen,text="Register",fg="black",bg="orange",font = "vandara 12 bold",width=14,height=2,command=lambda:InsertData.result(reg_data))
        self.reg_btn1.grid(row=0,column=1,pady=(480,0))
        self.to_login = tk.Button(reg_screen,text="Already have an account? Login",fg="black",bg="white",font = "vandara 10 bold",command=lambda:[self.reg_screen.destroy(),self.loginScreen(tk.Tk())],relief=FLAT,height=2)
        self.to_login.grid(row=1,column=1)

    

#This class will run when self.reg_btn1 has been clicked!
#Insert data from user input register form into database
class InsertData:
    def result(data):
        for i,items in enumerate(data):
            if items.get() == "":
                if i == 0 and items.get() == "":
                    messagebox.showwarning("Admin:","Please input username!")
                    return
                elif i == 1 and items.get() == "":
                    messagebox.showwarning("Admin:","Please input Password!")
                    return
                elif i == 2 and items.get() == "":
                    messagebox.showwarning("Admin:","Please input Confirm Password!")
                    return
                elif i == 3 and items.get() == "":
                    messagebox.showwarning("Admin:","Please input Name!")
                    return
                elif i == 4 and items.get() == "":
                    messagebox.showwarning("Admin:","Please input Email!")
                    return
                elif i == 5 and items.get() == "":
                    messagebox.showwarning("Admin:","Please input Phone!")
                    return
        if data[1].get() != data[2].get():
            messagebox.showwarning("Admin:","Password and Confirm Passoword does not match!")
        else :
            pwd = data[1].get()
            encodePwd = hashlib.md5(pwd.encode()).hexdigest() #Encrypt password 
            try :
                conn = lite.connect('db/iStock.db')
                curs = conn.cursor()
                print("Success")
                query_reg_insert = """INSERT INTO users (username,password,name,email,phone)
                VALUES(?,?,?,?,?)"""
                curs.execute(query_reg_insert,[data[0].get(),encodePwd,data[3].get(),data[4].get(),data[5].get()])
                conn.commit()
                conn.close()
            except Error :
                messagebox.showwarning("Admin:","Username already exists!\nPlease try again")

#This class will run when self.login has been clicked 
#When user login this class will check data in database 
class LoginCheck:
    def searchData(uname,pwd):
        conn = lite.connect('db/iStock.db')
        curs = conn.cursor()
        query_search_data =  "SELECT * FROM users where username = ? and password = ?"
        decodePwd = hashlib.md5(pwd.encode()).hexdigest() #Decrypt password 
        curs.execute(query_search_data,[uname,decodePwd])
        loginData = curs.fetchone()
        conn.close()
        if not loginData:
            print("Fail")
        else :
            Home()

if __name__ == '__main__':
    root = tk.Tk()
    main_app =  MainAuthen(root)
    root.mainloop()