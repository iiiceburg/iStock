import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tkinter import *
from tkinter import ttk
from sqlite3 import Error
from db.dbConnect import *
from view.authen import *
from notify.lineNotify import *
import webbrowser

class GetUserToken:
    def lineToken():
        global lblStatus,popup
        popup = tk.Toplevel()
        popup.title("Connect Line notify")
        popup.geometry("450x250+700+200")
        popup.resizable(0,0)
        popup.rowconfigure((0,1),weight=1)
        popup.columnconfigure((0),weight=1)
        popup.configure(bg="white")
       # popup.wm_title("Line notify")
        lblEnterToken = tk.Label(popup,text="Enter Line access token",font="Kanit 16 bold",fg="#333333",bg="white")
        lblEnterToken.grid(row=0,columnspan=3,sticky=N,pady=(25,0))

        lblStatus = tk.Label(popup,font="Kanit 12",fg="#333333",bg="white")
        lblStatus.grid(row=1,columnspan=3)

        tokenEntry = tk.Text(popup,font="Lato 12",fg="#333333",height = 2, width = 40,bg="lightgrey",relief=FLAT)
        tokenEntry.grid(row=0,columnspan=3,sticky=S)

        tk.Button(popup,text="Connect",fg="white",font="Kanit 14",bg="#07BF3F",relief=FLAT,command=lambda:checkStatus(tokenEntry.get(1.0, "end-1c"))).grid(row=1,columnspan=3,sticky=N,pady=(15,0))
        tk.Button(popup,text="How to connect line notify?",fg="#333333",font="Kanit 12 bold",bg="white",relief=FLAT,command=ContactUs.callurl).grid(row=1,columnspan=3,pady=(40,0))

       # tk.Button(popup, text="Connect",fg="white",font="Kanit 14",bg="#07BF3F",relief=FLAT,command=lambda:notify(tokenEntry.get(1.0, "end-1c"))).grid(row=1,columnspan=3,sticky=N,pady=(15,0))

    global checkStatus   
    def checkStatus(token):
        status = LineNotify.notify("Test connection",token)
        if not token:
            messagebox.showwarning(parent=popup,title="iStock",message="Please Enter access token")
            return
        else :
            if status == 200:
                try:
                    conn = connect_sqLite()
                    curs = conn.cursor()
                    curs.execute("INSERT INTO lineTokens(user_id,tokens) VALUES(?,?)",[userData[0],token])
                    conn.commit()
                    conn.close()
                    messagebox.showinfo(parent=popup,title="iStock",message="Connection has been successful")
                except Error:
                    messagebox.showwarning(parent=popup,title="iStock",message="You already connected to Line notify")
            else :
                messagebox.showwarning(parent=popup,title="iStock",message="Connection failed , Access token is invalid\nPlease try again.")
                return
                
                
    #Get current user token
    def notify(msg):
        conn = connect_sqLite()
        curs = conn.cursor()
        curs.execute("SELECT * FROM lineTokens WHERE user_id = ?",[userData[0]])
        user_token = curs.fetchone() # => user_token[1] get user token
        conn.close()
        if not user_token:
            pass
        else:
            LineNotify.notify(msg,user_token[1])
        # print(user_token[1])

class ContactUs:
    def callurl():
        webbrowser.open("https://lin.ee/AgxEZ6p")

class Home:
    global currentUser
    def __init__(self,currentUser):
        global userData
        userData = currentUser
        self.window = tk.Tk()
        self.window.title("Welcome to istock : %s"%currentUser[1])
        self.window.geometry("1280x800+300+0")
        self.window.resizable(0,0)
        self.window.option_add("*Font", "Vandara 10")
        self.window.rowconfigure((0,1),weight=1)
        self.window.columnconfigure((0,1),weight=1)
        self.window.iconphoto(False, tk.PhotoImage(file="./assets/logo.png"))
        menuBar = Menu(self.window)
                # menu.add_separator()
        menuBar.add_cascade(label="Line notify",command=GetUserToken.lineToken)
        menuBar.add_cascade(label="Contact Us",command=ContactUs.callurl)
        menuBar.add_cascade(label="Exit",command=lambda:[self.window.destroy()])
        self.window.config(menu=menuBar)

        self.searchFrm = tk.LabelFrame(self.window, text="Product Search",fg="#333333",font="Kanit 16")
        self.searchFrm.place(x=0,y=425,width=500,height=180)

        self.CategoryFrm = tk.LabelFrame(self.window, text="Category Management",fg="#333333",font="Kanit 16")
        self.CategoryFrm.place(x=0,y=585,width=500,height=195)

        self.productFrm = tk.LabelFrame(self.window, text="Products Management",fg="#333333",font="Kanit 16")
        self.productFrm.place(x=500,y=425,width=780,height=355)

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

        self.scrollbar = tk.Scrollbar(self.treeviewFrm)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        
        self.treeview = ttk.Treeview(self.treeviewFrm,columns=("no","id","sku","product_name","category","quantity","price"),yscrollcommand=self.scrollbar.set,height=20)
        self.treeview.pack(fill="x")

        self.scrollbar.config(command=self.treeview.yview)

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
        self.treeview.column("price",width=170,minwidth=170,anchor=CENTER)

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

    #Query category by user_id
    global query_ctg
    def query_ctg():
        ctg_list = []
        conn = connect_sqLite()
        curs = conn.cursor()
        curs.execute("SELECT * FROM products_category WHERE user_id = ?",[userData[0]])
        ctgs = curs.fetchall()
        conn.close()
        for ctg in ctgs:
            ctg_list.append("%s %s"%(ctg[1],ctg[2]))
        return ctg_list

    global search_filter
    def search_filter(self):
        global ctg_search
        searchFrm = self.searchFrm
        tk.Label(searchFrm,text="Category :",fg="#333333",font="kanit 14").place(x=10,y=10)
        tk.Label(searchFrm,text="Filter by :",fg="#333333",font="kanit 14").place(x=21,y=50)
        tk.Label(searchFrm,text="Search :",fg="#333333",font="kanit 14").place(x=27,y=100)

        ctg_search = ttk.Combobox(searchFrm,width=20,height=5,font="vandara 14",state="readonly",justify=CENTER)
        ctg_search['values'] = query_ctg()
        ctg_search.place(x=120,y=15)

        radioBtn_val = StringVar()
        radioBtn_val.set("0")
        searchmenu1 = tk.Radiobutton(searchFrm,text="Product Name",value="0",variable=radioBtn_val)
        searchmenu1.place(x=120,y=55)

        searchmenu2 = tk.Radiobutton(searchFrm,text="Product SKU",value="1",variable=radioBtn_val)
        searchmenu2.place(x=250,y=55)

        searchbar = tk.Entry(searchFrm,foreground="#333333",font="kanit 16")
        searchbar.place(x=120,y=100)

        tk.Button(searchFrm,text="Find result",font="kanit 14 bold",bg="orange",fg="black",relief=FLAT,command=lambda:find_result(ctg_search.get(),radioBtn_val.get(),searchbar.get())).place(x=370,y=92)
        tk.Label(searchFrm,text="Search :",fg="#333333",font="kanit 14").place(x=27,y=100)

        def find_result(ctg,fillterBy,search):
            conn = connect_sqLite()
            curs = conn.cursor()
            if not ctg:
                if fillterBy == "0":
                    curs.execute("SELECT * from products WHERE user_id = ? AND product_name LIKE ?",[userData[0],search+"%"])
                    products = curs.fetchall()
                    conn.close()
                    if not products:
                        messagebox.showwarning("iStock:","Item not found\nPlease try again.")
                        return
                    self.treeview.delete(*self.treeview.get_children())
                    for i,product in enumerate(products):
                        productTreeview = self.treeview
                        productTreeview.insert("","end",values=(i+1,product[1],product[2],product[3],product[4],product[5],product[6]))
                else :
                    curs.execute("SELECT * from products WHERE user_id = ? AND sku LIKE ?",[userData[0],search+"%"])
                    products = curs.fetchall()
                    conn.close()
                    if not products:
                        messagebox.showwarning("iStock:","Item not found\nPlease try again.")
                        return
                    self.treeview.delete(*self.treeview.get_children())
                    for i,product in enumerate(products):
                        productTreeview = self.treeview
                        productTreeview.insert("","end",values=(i+1,product[1],product[2],product[3],product[4],product[5],product[6]))
            else:
                if not search:
                    curs.execute("SELECT * FROM products WHERE user_id = ? and category = ?",[userData[0],ctg])
                    products = curs.fetchall()
                    conn.close()
                    if not products:
                        messagebox.showwarning("iStock:","Item not found\nPlease try again.")
                        return
                    self.treeview.delete(*self.treeview.get_children())
                    for i,product in enumerate(products):
                        productTreeview = self.treeview
                        productTreeview.insert("","end",values=(i+1,product[1],product[2],product[3],product[4],product[5],product[6]))                
                else:
                    if fillterBy == "0":
                        curs.execute("SELECT * from products WHERE user_id = ? AND category = ? AND product_name LIKE ?",[userData[0],ctg,search+"%"])
                        products = curs.fetchall()
                        conn.close()
                        if not products:
                            messagebox.showwarning("iStock:","Item not found\nPlease try again.")
                            return
                        self.treeview.delete(*self.treeview.get_children())
                        for i,product in enumerate(products):
                            productTreeview = self.treeview
                            productTreeview.insert("","end",values=(i+1,product[1],product[2],product[3],product[4],product[5],product[6]))
                    else :
                        curs.execute("SELECT * from products WHERE user_id = ? AND category = ? AND sku LIKE ?",[userData[0],ctg,search+"%"])
                        products = curs.fetchall()
                        conn.close()
                        if not products:
                            messagebox.showwarning("iStock:","Item not found\nPlease try again.")
                            return
                        self.treeview.delete(*self.treeview.get_children())
                        for i,product in enumerate(products):
                            productTreeview = self.treeview
                            productTreeview.insert("","end",values=(i+1,product[1],product[2],product[3],product[4],product[5],product[6]))
            searchbar.delete(0,END)
            ctg_search.set("") 
 
    global current_ctg
    def current_ctg(event):
        global get_nameCtg
        current = catgDropdown.current()
        catgEntry.delete(0,END)
        currentCtg = query_ctg()[current]
        get_nameCtg = currentCtg.split()
        catgEntry.insert(0,get_nameCtg[1])       

    global category_management
    def category_management(self):
        global catgDropdown,catgEntry
        catgFrm = self.CategoryFrm
        tk.Label(catgFrm,text="Category :",fg="#333333",font="kanit 14").place(x=10,y=20)
        catgDropdown = ttk.Combobox(catgFrm,width=20,height=5,font="vandara 14",state="readonly",justify=CENTER)
        catgDropdown['values'] = query_ctg()
        catgDropdown.place(x=200,y=20)

        tk.Label(catgFrm,text="Category Name :",fg="#333333",font="kanit 14").place(x=10,y=70)   
        catgEntry = tk.Entry(catgFrm,foreground="#333333",font="kanit 16")
        catgEntry.place(x=200,y=70)

        tk.Button(catgFrm,text="Add Category",font="kanit 12 bold",bg="orange",fg="black",relief=FLAT,command=lambda:add_ctg(catgEntry.get())).place(x=10,y=120)
        tk.Button(catgFrm,text="Update Category",font="kanit 12 bold",bg="orange",fg="black",relief=FLAT,command=lambda:update_ctg(catgEntry.get())).place(x=170,y=120)
        tk.Button(catgFrm,text="Delete Category",font="kanit 12 bold",bg="orange",fg="black",relief=FLAT,command=lambda:delete_ctg(catgEntry.get())).place(x=350,y=120)
        catgDropdown.bind("<<ComboboxSelected>>",current_ctg)

        def add_ctg(name):
            if not name:
                messagebox.showwarning("Admin:","Please enter category name")
                return
            conn = connect_sqLite()
            curs = conn.cursor()
            curs.execute("INSERT INTO products_category(user_id,category) VALUES(?,?)",[userData[0],name])
            conn.commit()
            conn.close()
            messagebox.showinfo("iStock","Category added successfully")
            catgEntry.delete(0,END)   
            catgDropdown.set("")
            catgDropdown['values'] = query_ctg()
            category['values'] = query_ctg()
            ctg_search['values'] = query_ctg()

        def update_ctg(name):
            if not name:
                messagebox.showwarning("Admin:","Please enter category name")
                return
            conn = connect_sqLite()
            curs = conn.cursor()
            curs.execute("UPDATE products_category SET category = ? WHERE category_id = ?",[name,get_nameCtg[0]])
            conn.commit()
            conn.close()
            messagebox.showinfo("iStock","Category updated successfully") 
            catgEntry.delete(0,END)   
            catgDropdown.set("")
            catgDropdown['values'] = query_ctg()
            category['values'] = query_ctg()
            ctg_search['values'] = query_ctg()

        def delete_ctg(name):
            if not name:
                messagebox.showwarning("Admin:","Please enter category name")
                return
            conn = connect_sqLite()
            curs = conn.cursor()
            curs.execute("DELETE FROM products_category WHERE category_id = ?",[get_nameCtg[0]])
            conn.commit()
            conn.close()        
            messagebox.showinfo("iStock","Category deleted successfully") 
            catgEntry.delete(0,END)   
            catgDropdown.set("")
            catgDropdown['values'] = query_ctg()
            category['values'] = query_ctg()
            ctg_search['values'] = query_ctg()
              
    global product_management
    def product_management(self):
        global category
        productFrm = self.productFrm

        tk.Label(productFrm,text="Product SKU :",fg="#333333",font="kanit 14").place(x=10,y=50)
        skuEntry = tk.Entry(productFrm,foreground="#333333",font="kanit 16",width=15,justify=CENTER)
        skuEntry.place(x=140,y=50)

        tk.Label(productFrm,text="Product Name :",fg="#333333",font="kanit 14").place(x=350,y=50)
        nameEntry = tk.Entry(productFrm,foreground="#333333",font="kanit 16",justify=CENTER)
        nameEntry.place(x=490,y=50)

        tk.Label(productFrm,text="Category:",fg="#333333",font="kanit 14").place(x=10,y=130)
        category = ttk.Combobox(productFrm,width=15,height=5,font="vandara 14",state="readonly",justify=CENTER)
        category['values'] = query_ctg()
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
            messagebox.showinfo("iStock","Product added successfully")                
            skuEntry.delete(0,END)
            nameEntry.delete(0,END)
            category.set("")
            qtyEntry.delete(0,END)
            prcEntry.delete(0,END)
            retrieve_data()
            msg = "%s\nคำสั่ง : เพิ่มสินค้า\nชื่อสินค้า : %s\nรหัส SKU : %s\nหมวดหมู่ : %s\nจำนวน : %s\nราคา : %s"%(userData[1],name,sku,catg,qty,prc)
            GetUserToken.notify(msg)    

        def updateProduct(sku,name,catg,qty,prc):
            values = self.treeview.item(self.treeview.focus(),'values')
            conn = connect_sqLite()
            curs = conn.cursor()
            curs.execute("UPDATE products SET sku=?,product_name=?,category=?,quantity=?,price=? WHERE product_id = ?",[sku,name,catg,qty,prc,values[1]])
            conn.commit()
            conn.close()  
            messagebox.showinfo("Admin:","Update stock successfully!")
            skuEntry.delete(0,END)
            nameEntry.delete(0,END)
            category.set("")
            qtyEntry.delete(0,END)
            prcEntry.delete(0,END)
            retrieve_data()
            msg = "%s\nคำสั่ง : อัพเดทสินค้า\nชื่อสินค้า : %s\nรหัส SKU : %s\nหมวดหมู่ : %s\nจำนวน : %s\nราคา : %s"%(userData[1],name,sku,catg,qty,prc)
            GetUserToken.notify(msg)

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
                msg = "%s\nคำสั่ง : ลบสินค้า\nชื่อสินค้า : %s\nรหัส SKU : %s\nหมวดหมู่ : %s\nจำนวน : %s\nราคา : %s"%(userData[1],values[3],values[2],values[4],values[5],values[6])
                GetUserToken.notify(msg)

        def clearAll():
            skuEntry.delete(0,END)
            nameEntry.delete(0,END)
            category.set("")
            qtyEntry.delete(0,END)
            prcEntry.delete(0,END)

        self.treeview.bind("<Double-1>",treeViewClick)




