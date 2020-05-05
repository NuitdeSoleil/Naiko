from tkinter import *
from bouton import *
from json1 import *

print("Salut les gens je m'appelle Naïko!")
print("Et je suis une assitante virtuel!")

print("le systeme pricipale est prêts!")
print(json.dumps(x, indent=4))

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
