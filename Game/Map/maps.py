import sys
import os.path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Game.items import eat_items as eat
from chachka import Chachka
from Game.game import Game

class Map:
    def __init__(self, x1, x2, z1, z2):
        self.x1, self.x2 = x1, x2
        self.z1, self.z2 = z1, z2
        self.objects = []
        self.eat = []
        self.chaks = []
        Game.maps.append(self)
    def link_chack(self, chachka: Chachka):
        if isinstance(chachka, Chachka):
            chack_x = max(self.x1, min(chachka.x, self.x2))
            chack_z = max(self.z1, min(chachka.z, self.z2))
            chachka.x, chachka.z = chack_x, chack_z
            self.objects.append(chachka)
            self.chaks.append(chachka)
    def link_eat(self, food: eat.Base_Eat):
        if isinstance(food, eat.Base_Eat):
            eat_x = max(self.x1, min(food.x, self.x2))
            eat_z = max(self.z1, min(food.z, self.z2))
            food.x, food.z = eat_x, eat_z
            self.objects.append(food)
            self.eat.append(food)
