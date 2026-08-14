import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Game.Utils.cpp_utils.clamp import clamp_int as clamp

# типы еды (от которых идет наследование)

class Base_Eat:
    def __init__(self, x, z, eat):
        self.x, self.z = x, z
        self.eat = eat

class Filling_Eat(Base_Eat):
    def __init__(self, x, z, eat):
        super().__init__(x, z, clamp(30, eat, 80))

class Light_food(Base_Eat):
    def __init__(self, x, z, eat):
        super().__init__(x, z, clamp(3, eat, 25))

# Виды яблок

class Apple_slice(Light_food):
    def __init__(self, x, z, eat=7):
        super().__init__(x, z, clamp(4, eat, 9))
        
class Apple(Filling_Eat):
    def __init__(self, x, z, eat=30):
        super().__init__(x, z, clamp(25, eat, 40))
