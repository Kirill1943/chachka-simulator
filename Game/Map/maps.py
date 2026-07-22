import os
import sys

import rich

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Game.items import Eat_items as eat


class Map:
    def __init__(self, x1, x2, z1, z2):
        self.x1, self.x2 = x1, x2
        self.z1, self.z2 = z1, z2
        self.objects = []
        self.eat = []
        self.chaks = []

    def link_chack(self, chachka):
        if type(chachka).__name__ == "Chachka":
            chack_x = max(self.x1, min(chachka.x, self.x2))
            chack_z = max(self.z1, min(chachka.z, self.z2))
            chachka.x, chachka.z = chack_x, chack_z
            chachka.in_map = self
            self.objects.append(chachka)
            self.chaks.append(chachka)
        else:
            print('[#FF0000][ERROR][/] попытка расположить НЕ чачку на карте')

    def link_eat(self, food: eat.Base_Eat):
        if isinstance(food, eat.Base_Eat):
            eat_x = max(self.x1, min(food.x, self.x2))
            eat_z = max(self.z1, min(food.z, self.z2))
            food.x, food.z = eat_x, eat_z
            self.objects.append(food)
            self.eat.append(food)
    def get_object(self, x, z):
        try:
            x, z = int(x), int(z)
        except (ValueError, TypeError):
            rich.print('[#FFFF00][WARNING][/] Указаны неккоректные координаты для нахождения обьекта по координатам')
            return
        x = max(self.x1, min(x, self.x2))
        z = max(self.z1, min(z, self.z2))
        for i in self.objects:
            if i.x == x and i.z == z:
                return i