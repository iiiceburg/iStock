import tkinter as tk
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Home:
    def __init__(self):
        self.window = tk.Tk()
        self.window.state("zoomed")
        self.window.title("iStock ")
        self.window.mainloop()
        self.window.rowconfigure((0,1,2),weight=1)
        self.window.columnconfigure((0,1,2),weight=1)
        # self.data = data

    
    def menuBar(self):
        print(self.currentUser)

    def header(self): #Search
        pass

    def productList(self):
        pass

class Product:
    def __init__(self):
        pass

    def filterSearch(self):
        pass

    def refresh(self):
        pass

    def insertProduct(self):
        pass

    def updateProcut(self):
        pass

    def deleteProduct(self):
        pass


if __name__ == '__main__':
    app = Home()  
