import os
import sys

import rich

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import Game.chachka_reanimation as reanim
from Game.Utils.cpp_math import chachka_math
from Game.Utils.cpp_utils.clamp import clamp_int as clamp
from Game.Utils.ScanTools.scan import scan_map
from Game.Utils.SortTools.sort_objects import sort_eat, sort_potions


class Chachka:
    def __init__(self, age, x, z):
        self.x, self.z = x, z
        self.age = age
        self.hp = 100
        self.stamina = 100
        self.eat = 100
        self.in_map = ...
        self.alive = True
        self.inventory = []
        self.__size = [6, 6, 6]

    def Viy(self, scream: int = 2):
        if self.alive:
            scream = clamp(1, scream, 5)
            print(f"Чачка викает: В{'И' * scream}")

    def Scream(self, scream: int = 10):
        if self.alive:
            scream = clamp(8, scream, 15)
            print(f"Чачка орет: В{'И' * scream}")
    def use_potions(self, radius=1):
        if self.alive:
            try:
                radius = clamp(1, abs(int(radius)), 3)
            except (ValueError, TypeError):
                radius = 1
            if self.in_map is None:
                rich.print('[#FFFF00][WARNING][/] чачка не привязана к карте')
            else:
                potions = sort_potions(scan_map(distance=radius, Map=self.in_map, chachka_x=self.x, chachka_z=self.z))
                for i in potions:
                    i.use(self)

                self.in_map.potions = [p for p in self.in_map.potions if p not in potions]
                self.in_map.objects = [o for o in self.in_map.objects if o not in potions]
    def eating(self, radius=3):
        if self.alive:
            try:
                radius = clamp(1, abs(int(radius)), 3)
            except (ValueError, TypeError):
                radius = 3
            if self.in_map is None:
                rich.print('[#FFFF00][WARNING][/] чачка не привязана к карте')
            else:
                eat = sort_eat(scan_map(distance=radius, Map=self.in_map, chachka_x=self.x, chachka_z=self.z))
                for i in eat:
                    self.eat += i.eat
                    self.eat = clamp(0, self.eat, 100)
                    if i in self.in_map.objects:
                        self.in_map.objects.remove(i)
    def step(self, x, z):
        if self.alive:
            x = clamp(-3, x, 3)
            z = clamp(-3, z, 3)
            self.x += x
            self.z += z

            self.x = clamp(self.in_map.x1, self.x, self.in_map.x2)
            self.z = clamp(self.in_map.x1, self.x, self.in_map.x2)

            minus_stamina = chachka_math.calculate_stamina(x, z)

            if self.stamina - minus_stamina <= 0:
                self.stamina = 0
                self.hp -= chachka_math.calculate_removed_hp(self.stamina, minus_stamina)
                
                if self.hp <= 0:
                    self.stamina, self.hp = 0, 0
                    self.alive = False
                    print("чачка умерла.. но ты подбежал к чачке, ШАНС ЕСТЬ!")
                    reanim.reanim(self)
            else:
                self.stamina -= minus_stamina
    def set_size(self, size: list):
        self.__size = size
