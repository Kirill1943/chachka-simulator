import os
import sys
import typing

import rich

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Game.items import Eat_items as eat
from Game.items import Potion_items as potions
from Game.Utils.cpp_utils.clamp import clamp_int as clamp

if typing.TYPE_CHECKING:
    from Game import Chachka

class Map:
    def __init__(self, x1, x2, z1, z2):
        self.x1, self.x2 = x1, x2
        self.z1, self.z2 = z1, z2
        self.gen_type = None
        self.objects = []
        self.eat = []
        self.chaks = []
        self.potions = []

    def link_chack(self, chachka: Chachka.Chachka):
        if type(chachka).__name__ == "Chachka":
            chack_x = clamp(self.x1, chachka.x, self.x2)
            chack_z = clamp(self.z1, chachka.z, self.z2)
            chachka.x, chachka.z = chack_x, chack_z
            chachka.in_map = self
            self.objects.append(chachka)
            self.chaks.append(chachka)
        else:
            print('[#FF0000][ERROR][/] попытка расположить НЕ чачку на карте')
    def link_potion(self, potion):
        if isinstance(potion, potions.potion):
            potion_x = clamp(self.x1, potion.x, self.x2)
            potion_z = clamp(self.z1, potion.x, self.z2)
            potion.x, potion.z = potion_x, potion_z
            self.objects.append(potion)
            self.potions.append(potion)

    def link_eat(self, food: eat.Base_Eat):
        if isinstance(food, eat.Base_Eat):
            eat_x = clamp(self.x1, food.x, self.x2)
            eat_z = clamp(self.z1, food.z, self.z2)
            food.x, food.z = eat_x, eat_z
            self.objects.append(food)
            self.eat.append(food)
    def get_object(self, x, z):
        try:
            x, z = int(x), int(z)
        except (ValueError, TypeError):
            rich.print('[#FFFF00][WARNING][/] Указаны неккоректные координаты для нахождения обьекта по координатам')
            return
        x = clamp(self.x1, x, self.x2)
        z = clamp(self.z1, z, self.z2)
        for i in self.objects:
            if i.x == x and i.z == z:
                return i