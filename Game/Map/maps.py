import sys
import os.path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Game.items import eat_items as eat
from chachka import Chachka

class Map:
    def __init__(self, x1, x2, z1, z2):
        self.x1, self.x2 = x1, x2
        self.z1, self.z2 = z1, z2
        self.objects = []
        self.eat = []
        self.chaks = []
    def link_chack(self, chachka: Chachka):
        if isinstance(chachka, chachka):
            chack_x = max(self.x1, min(chachka.x, self.x2))
            chack_z = max(self.z1, min(chachka.z, self.z2))
            chachka.x, chachka.z = chack_x, chack_z
            self.objects.append(chachka)
            self.chaks.append(chachka)
    def link_eat(self, eat: eat.Base_eat):
        if isinstance(eat, eat.Base_eat):
            eat_x = max(self.x1, min(eat.x, self.x2))
            eat_z = max(self.z1, min(eat.z, self.z2))
            eat.x, eat.z = eat_x, eat_z
            self.objects.append(eat)
            self.eat.append(eat)
