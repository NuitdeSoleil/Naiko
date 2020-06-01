from tkinter import *
import tkinter as tk
from tkinter import messagebox


nombre_lancement = 0
print(nombre_lancement + 1)

print("Salut les gens je m'appelle Naïko!")
print("Et je suis une assitante virtuel!")

print("le systeme pricipale est prêts!")
#print(json.dumps(x, indent=4))


def soon():
    tk.messagebox.showwarning("Désolé...", "Cette feature vas bientôt être disponible ! :(")


def settings():
    sett = Tk()
    sett.title("Settings")
    sett.geometry("800x480")
    sett.config(background='#830202')
    lb = Listbox(sett, width=10, height=5)
    lb.insert(1, "")
    lb.pack()
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


class Main():
    ac = Tk()
    ac.geometry("800x480")
    ac.config(background='black')
    ac.title("   ")
    photodiscord = PhotoImage(file='naïko/main/assets/discord.png')
    photosetings = PhotoImage(file='naïko/main/assets/settings.png')
    photoyoutube = PhotoImage(file='naïko/main/assets/youtube.png')
    photocalendrier = PhotoImage(file='naïko/main/assets/calendrier.png')
    photocam = PhotoImage(file='naïko/main/assets/cam.png')
    photogavit = PhotoImage(file='naïko/main/assets/gravit.png')


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
    asett.place(x=45, y=60)
    adisc.place(x=250, y=60)
    acalle.place(x=450, y=60)
    aRV.place(x=625, y=60)
    aYT.place(x=45, y=300)
    aGR.place(x=250, y=300)
    aApv.place(x=625, y=300)
    a8.place(x=450, y=300)
    ahelp.place(x=735, y=450)


    ac.mainloop()
    #wesh wesh canne a peche
