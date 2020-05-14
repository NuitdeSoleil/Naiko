import urwid 
import time


class Horloge:
    def __init__(self):
        self.configurer_horloge()
        self.palette = [('horloge', 'drak blue', '')]
        self.boucle = urwid.Mainloop(
            self.horloge,
            palette=self.palette
        self.boucle.set_alarm_in(1, self.actualiser)

    def configurer_horloge(self):
        text = time.strftime('%H:%M:%S')