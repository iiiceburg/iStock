import tkinter as tk
from tkinter import messagebox
from tkinter.constants import *
from tkinter import Frame, PhotoImage, Place, READABLE, ttk
import os, sys
from tkinter import font
from tkinter.constants import ACTIVE, BOTH, DISABLED, LEFT, TRUE, X, Y
from tkinter.messagebox import showwarning
from db.dbConnect import *
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Home:
    global currentUser
    def __init__(self,currentUser):
        global userData
        userData = currentUser
        self.window = tk.Tk()
        icon = PhotoImage(file="./assets/logo.png")
        self.window.iconphoto(False,icon)
        # self.window.state("zoomed")
        self.window.title("Welcome to istock : %s"%currentUser[1])
        self.window.geometry("1280x1000+300+0")
        self.window.resizable(0,0)
        self.window.option_add("*Font", "Vandara 10")
        self.window.rowconfigure((0,1,2),weight=1)
        self.window.columnconfigure((0,1,2),weight=1)

        self.searchFrm = tk.LabelFrame(self.window, text="Product Search",fg="#333333",font="Kanit 16")
        self.searchFrm.place(x=0,y=625,width=500,height=180)

        self.CategoryFrm = tk.LabelFrame(self.window, text="Category Management",fg="#333333",font="Kanit 16")
        self.CategoryFrm.place(x=0,y=805,width=500,height=195)

        self.productFrm = tk.LabelFrame(self.window, text="Products Management",fg="#333333",font="Kanit 16")
        self.productFrm.place(x=500,y=625,width=780,height=375)

        treeview(self)
        search_filter(self)
        category_management(self)
        product_management(self)
        self.window.mainloop()
        # self.data = data
    global treeview
    def treeview(self):
        self.treeviewFrm = Frame(self.window)
        self.treeviewFrm.place(x=0,y=0)
        
        self.treeview = ttk.Treeview(self.treeviewFrm,columns=("no","id","sku","product_name","category","quantity","price"),height=30)
        self.treeview.pack(fill="x")

        self.treeview.heading("#0")
        self.treeview.heading("no",text="No")
        self.treeview.heading("id",text="Product ID")
        self.treeview.heading("sku",text="SKU")
        self.treeview.heading("product_name",text="Product")
        self.treeview.heading("category",text="Category")
        self.treeview.heading("quantity",text="Qty")
        self.treeview.heading("price",text="price")

        self.treeview.column("#0",width=0,minwidth=0)
        self.treeview.column("no",width=50,minwidth=50,anchor=CENTER)
        self.treeview.column("id",width=100,minwidth=100,anchor=CENTER)
        self.treeview.column("sku",width=100,minwidth=100,anchor=CENTER)
        self.treeview.column("product_name",width=490,minwidth=490)
        self.treeview.column("category",width=250,minwidth=250,anchor=CENTER)
        self.treeview.column("quantity",width=100,minwidth=100,anchor=CENTER)
        self.treeview.column("price",width=200,minwidth=200,anchor=CENTER)

        global retrieve_data
        def retrieve_data():
            conn = connect_sqLite()
            curs = conn.cursor()
            curs.execute("select * from products where user_id = ?",[userData[0]])
            products = curs.fetchall()
            conn.close()

            self.treeview.delete(*self.treeview.get_children())

            for i,product in enumerate(products):
                productTreeview = self.treeview
                productTreeview.insert("","end",values=(i+1,product[1],product[2],product[3],product[4],product[5],product[6]))

        retrieve_data()

    global search_filter
    def search_filter(self):
        searchFrm = self.searchFrm
        tk.Label(searchFrm,text="Category :",fg="#333333",font="kanit 14").place(x=10,y=10)
        tk.Label(searchFrm,text="Filter by :",fg="#333333",font="kanit 14").place(x=21,y=50)
        tk.Label(searchFrm,text="Search :",fg="#333333",font="kanit 14").place(x=27,y=100)

        category = ttk.Combobox(searchFrm,width=20,height=5,font="vandara 14",state="readonly",justify=CENTER)
        category['values'] = ("category1","category2","category3","category4")
        category.place(x=120,y=15)

        searchmenu1 = tk.Radiobutton(searchFrm,text="Product Name",value=0)
        searchmenu1.place(x=120,y=55)

        searchmenu2 = tk.Radiobutton(searchFrm,text="Product SKU",value=1)
        searchmenu2.place(x=250,y=55)

        searchbar = tk.Entry(searchFrm,foreground="#333333",font="kanit 16")
        searchbar.place(x=120,y=100)

        tk.Button(searchFrm,text="Find result",font="kanit 14 bold",bg="orange",fg="black",relief=FLAT).place(x=370,y=92)
        tk.Label(searchFrm,text="Search :",fg="#333333",font="kanit 14").place(x=27,y=100)
        
    global category_management
    def category_management(self):
        catgFrm = self.CategoryFrm
        tk.Label(catgFrm,text="Category Name :",fg="#333333",font="kanit 14").place(x=10,y=50)
        
        catgEntry = tk.Entry(catgFrm,foreground="#333333",font="kanit 16")
        catgEntry.place(x=170,y=50)

        tk.Button(catgFrm,text="Add Category",font="kanit 12 bold",bg="orange",fg="black",relief=FLAT).place(x=10,y=120)
        tk.Button(catgFrm,text="Update Category",font="kanit 12 bold",bg="orange",fg="black",relief=FLAT).place(x=170,y=120)
        tk.Button(catgFrm,text="Delete Category",font="kanit 12 bold",bg="orange",fg="black",relief=FLAT).place(x=350,y=120)
           
    global product_management
    def product_management(self):
        productFrm = self.productFrm

        tk.Label(productFrm,text="Product SKU :",fg="#333333",font="kanit 14").place(x=10,y=50)
        skuEntry = tk.Entry(productFrm,foreground="#333333",font="kanit 16",width=15,justify=CENTER)
        skuEntry.place(x=140,y=50)

        tk.Label(productFrm,text="Product Name :",fg="#333333",font="kanit 14").place(x=350,y=50)
        nameEntry = tk.Entry(productFrm,foreground="#333333",font="kanit 16",justify=CENTER)
        nameEntry.place(x=490,y=50)

        tk.Label(productFrm,text="Category:",fg="#333333",font="kanit 14").place(x=10,y=130)
        category = ttk.Combobox(productFrm,width=15,height=5,font="vandara 14",state="readonly",justify=CENTER)
        category['values'] = ("category1","category2","category3","category4")
        category.place(x=140,y=130)

        tk.Label(productFrm,text="Quantity :",fg="#333333",font="kanit 14").place(x=350,y=130)
        qtyEntry = tk.Entry(productFrm,foreground="#333333",font="kanit 16",width=7,justify=CENTER)
        qtyEntry.place(x=490,y=130)

        tk.Label(productFrm,text="Price :",fg="#333333",font="kanit 14").place(x=10,y=200)
        prcEntry = tk.Entry(productFrm,foreground="#333333",font="kanit 16",width=15,justify=CENTER)
        prcEntry.place(x=140,y=200)

        tk.Button(productFrm,text="Add Product",font="kanit 14 bold",bg="#333333",fg="orange",relief=FLAT,command=lambda:addProduct(userData[0],skuEntry.get(),nameEntry.get(),category.get(),qtyEntry.get(),prcEntry.get())).place(x=20,y=270)
        tk.Button(productFrm,text="Update Product",font="kanit 14 bold",bg="#333333",fg="orange",relief=FLAT,command=lambda:updateProduct(skuEntry.get(),nameEntry.get(),category.get(),qtyEntry.get(),prcEntry.get())).place(x=200,y=270)
        tk.Button(productFrm,text="Delete Product",font="kanit 14 bold",bg="#333333",fg="orange",relief=FLAT,command=lambda:delProduct()).place(x=400,y=270)
        tk.Button(productFrm,text="Clear All",font="kanit 14 bold",bg="#333333",fg="orange",relief=FLAT,command=lambda:clearAll()).place(x=600,y=270)

        global treeViewClick
        def treeViewClick(e):
            skuEntry.delete(0,END)
            nameEntry.delete(0,END)
            category.set("")
            qtyEntry.delete(0,END)
            prcEntry.delete(0,END)    
            values = self.treeview.item(self.treeview.focus(),'values')        
            skuEntry.insert(0,values[2])
            nameEntry.insert(0,values[3])
            category.set(values[4])
            qtyEntry.insert(0,values[5])
            prcEntry.insert(0,values[6])  

        #Insert new product
        def addProduct(u_id,sku,name,catg,qty,prc):
            if not name:
                messagebox.showwarning("Admin:","Please enter product name")
                return
            if not catg:
                messagebox.showwarning("Admin:","Please select category")
                return
            if not qty:
                messagebox.showwarning("Admin:","Please enter quantity")
                return
            if not prc:
                messagebox.showwarning("Admin:","Please enter price")
                return
            conn = connect_sqLite()
            curs = conn.cursor()
            curs.execute("INSERT INTO products(user_id,sku,product_name,category,quantity,price) VALUES(?,?,?,?,?,?)",[u_id,sku,name,catg,qty,prc])
            conn.commit()
            conn.close()
            skuEntry.delete(0,END)
            nameEntry.delete(0,END)
            category.set("")
            qtyEntry.delete(0,END)
            prcEntry.delete(0,END)
            messagebox.showinfo("iStock","Product added successfully")
            retrieve_data()

        def updateProduct(sku,name,catg,qty,prc):
            values = self.treeview.item(self.treeview.focus(),'values')
            conn = connect_sqLite()
            curs = conn.cursor()
            curs.execute("UPDATE products SET sku=?,product_name=?,category=?,quantity=?,price=? WHERE product_id = ?",[sku,name,catg,qty,prc,values[1]])
            conn.commit()
            conn.close()
            messagebox.showinfo("Admin:","Update stock successfully!")
            retrieve_data()

        # global delProduct
        def delProduct():
            msg = messagebox.askquestion ('Delete this course','Are you sure you want to delete this product?',icon = 'warning')
            if msg == "no":
                skuEntry.delete(0,END)
                nameEntry.delete(0,END)
                category.set("")
                qtyEntry.delete(0,END)
                prcEntry.delete(0,END)
            else:
                deleterow = self.treeview.selection()
                values = self.treeview.item(self.treeview.focus(),'values')
                conn = connect_sqLite()
                curs = conn.cursor()
                curs.execute("DELETE FROM products Where product_id = ?",[values[1]])
                conn.commit()
                conn.close()
                self.treeview.delete(deleterow)
                skuEntry.delete(0,END)
                nameEntry.delete(0,END)
                category.set("")
                qtyEntry.delete(0,END)
                prcEntry.delete(0,END)
                retrieve_data()
        
        def clearAll():
            skuEntry.delete(0,END)
            nameEntry.delete(0,END)
            category.set("")
            qtyEntry.delete(0,END)
            prcEntry.delete(0,END)
                

        self.treeview.bind("<Double-1>",treeViewClick)

      

