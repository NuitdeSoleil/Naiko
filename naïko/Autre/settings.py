from tkinter import *
import tkinter as tk
# nb: bien mettre le tkinter.messagebox, il n'est PAS importé par défaut !
import tkinter.messagebox


sett = Tk()
sett.geometry("800x480")
sett.title("Settings")
sett.config(background='#830202')

# wifi = Button(text="Wifi")
# wifi.pack()


class MenuBar(tk.Menu):
    def __init__(self, root):
    	#init of the super-class
        super().__init__(root)



def doSomething(self):
   print("Menu clicked")



menubar = tk.Menu(sett)

menuFile = Menu(menubar)
menuFile.add_command(label="New", command=doSomething)
menuFile.add_command(label="Open", command=doSomething)
menuFile.add_command(label="save", command=doSomething)
menuFile.add_separator()
menuFile.add_command(label="Exit", command=quit)
menuFile.add_cascade(label="File", menu=menuFile)

menuEdit = Menu(menubar)      
menuEdit.add_command(label="Undo", command=doSomething)
menuEdit.add_command(label="Copy", command=doSomething)
menuEdit.add_command(label="Cut", command=doSomething)
menuEdit.add_command(label="Paste", command=doSomething)
menuEdit.add_cascade(label="Edit", menu=menuEdit)


sett.config(menu = menubar)        



sett.mainloop()