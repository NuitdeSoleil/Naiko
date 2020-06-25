import glob
import sys
import os
from tkinter import *

print('Test')

class PiVision(Tk):
    def __init__(self, images):
        Tk.__init__(self)
        self.creer_composant()
        if len(images) > 0:
            self.initialiser_images()
            self.afficher_image()
        else:
            self.afficher_erreur()
        self.mainloop()

    def creer_composant(self):
        self.composant_image = Label(self)
        self.composant_image.pack(expand=YES, fill=BOTH)
        self.button_frame = Frame(self)
        self.bouton_frame.pack(side=BOTTOM)
        self.bouton_precedent = Button(self.button_frame,  text='Suivant', command=lambda:self.image_precedente())
        self.bouton_precedent.pack




if __name__ == "__main__.py":
    def usage(message=''):
        print(message)
        sys.exit(1)
    if len(sys.argv) != 2:
        usage('Veuillez indiquez un répertoire!')
    repertoire = sys.argv[1]
    if not os.path.isidir(repertoire):
        usage("\"{r}\"N'est pas un répertoire!" ).format(r=repertoire)
        extensions = 'png jpg jpeg gif'.split()
        extensions = extensions + list(map(str.upper, extensions))
        images = []

        for ext in extensions:
            images.append(glob.glob('{}/*.{}'.format(repertoire, ext)))

        images = sum(images, [])
        PiVision(images)