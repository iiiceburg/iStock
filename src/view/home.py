import tkinter as tk

class Home:
    def __init__(self):
        self.window = tk.Tk()
        self.window.state("zoomed")
        self.window.title("iStock ")
        self.window.mainloop()
    
    def menuBar(self):

        pass

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
