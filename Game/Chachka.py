import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import Game.chachka_reanimation as reanim


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
            scream = min(5, max(1, scream))
            print(f"Чачка викает: В{'И' * scream}")

    def Scream(self, scream: int = 10):
        if self.alive:
            scream = min(15, max(8, scream))
            print(f"Чачка орет: В{'И' * scream}")

    def eating(self):
        if self.alive:
            print("Чачка ест")
            self.eat += 3
            self.eat = max(0, min(self.eat, 100))

    def step(self, x, z):
        if self.alive:
            x, z = max(-3, min(x, 3)), max(-3, min(z, 3))
            self.x += x
            self.z += z

            self.x = max(self.in_map.x1, min(self.x, self.in_map.x2))
            self.z = max(self.in_map.z1, min(self.z, self.in_map.z2))

            minus_stamina = (abs(x) + abs(z)) / 100 * 40

            if self.stamina - minus_stamina <= 0:
                overuse = minus_stamina - self.stamina
                self.stamina = 0
                self.hp -= overuse / 100 * 150
                
                if self.hp <= 0:
                    self.stamina, self.hp = 0, 0
                    self.alive = False
                    print("чачка умерла.. но ты подбежал к чачке, ШАНС ЕСТЬ!")
                    reanim.reanim(self)
            else:
                self.stamina -= minus_stamina

    def set_size(self, size: list):
        self.__size = size