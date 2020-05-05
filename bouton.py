#from main import *
import tkinter as tk
from tkinter import *
import tkinter.messagebox    
#import premierepage


print("Le sytème des bouton est près!")


def soon():
    tk.messagebox.showwarning("Désolé...", "Cette feature vas bientôt être disponible ! :(")

def settings():
    sett = Tk()
    sett.title("Settings")
    sett.geometry("800x480")
    sett.config(background='#830202')
    sett.mainloop()    

def discord():
    disc = Tk()
    disc.title("Discord")
    disc.geometry("800x480")
    disc.config(background='#830202')
    disc.mainloop() 
def youtube():
    you = Tk()
    you.title("Youtube")
    you.geometry("800x480")
    you.config(background='#830202')
    you.mainloop() 
def about():
    tk.messagebox.showinfo("Naïko", "Naïko est un assistant virtuel qui est utile dans la vie de tout les jours")

def Gravit():
    grav = Tk()
    grav.title("gravit")
    grav.geometry("800x480")
    grav.config(background='#830202')
    grav.mainloop() 
def maj():
    tk.messagebox.showerror("Attention", "Cette zone est en maintenance! Veuillez réessayé ulterieurment!")

def acceuil():
    #wind.destroy()

    ac = Tk()
    ac.geometry("800x480")
    ac.config(background='#830202')
    ac.title("   ")
    photodiscord = PhotoImage(file='assets/discord.png')
    photosetings = PhotoImage(file='assets/settings.png')
    photoyoutube = PhotoImage(file='assets/youtube.png')
    photocalendrier = PhotoImage(file='assets/calendrier.png')
    photocam = PhotoImage(file='assets/cam.png')
    photogavit = PhotoImage(file='assets/gravit.png')


    #on crée tous nos boutton avec les bonne couleur 
    asett = Button(ac, text=("SETTINGS"), bg='black', fg='white', command=settings, image=photosetings)
    adisc = Button(ac, text=("DISCORD"), bg='black', fg='white', command=discord, image=photodiscord)
    acalle = Button(ac, text=("CALENDRIER"), bg='black', fg='white', command=soon, image=photocalendrier)
    aRV = Button(ac, text=("RETOUR VIDÉO"), bg='black', fg='white', command=maj, image=photocam)
    aYT = Button(ac, text=("YOUTUBE"), bg='black', fg='white', command=youtube, image=photoyoutube)
    aGR = Button(ac, text=("GRAVIT"), bg='black', fg='white', command=Gravit, image=photogavit )
    aApv = Button(ac, text=("APPELLE VIDÉO"), bg='black', fg='white', command=soon, image=photocam)
    a8 = Button(ac, text=("APP N°8"), bg='black', fg='white', command=soon)
    ahelp = Button(ac, text=("about"), bg='black', fg='white', command=about)

    #on fixe sur la grille tous nos boutton
    asett.place(x=30, y=30)
    adisc.place(x=179, y=30)
    acalle.place(x=334, y=30)
    aRV.place(x=467, y=30)
    aYT.place(x=30, y=200)
    aGR.place(x=185, y=200)
    aApv.place(x=467, y=200)
    a8.place(x=345, y=200)
    ahelp.place(x=735, y=450)


    ac.mainloop()