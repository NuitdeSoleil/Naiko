from tkinter import *
import tkinter as tk
from tkinter import messagebox
 
def soon():
    tk.messagebox.showwarning("Désolé...", "Cette feature va bientôt être disponible ! :(")


regl = Tk()
regl.geometry("800x480")
regl.config(background='black')

droite = Frame(regl, borderwidth=2, relief=GROOVE)
droite.config(background='white')
droite.place(x=30, y=150)

apparence = Button(droite, text='apparence', command=soon)
apparence.pack()

test = Label(droite, text='text')
test.pack()




l = Label(regl, text="Vous vous situez dans les réglage de votre appraeil Naïko", bg='black', fg='white')
l.pack()

regl.mainloop()