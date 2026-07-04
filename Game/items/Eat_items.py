

# типы еды (от которых идет наследование)

class Base_Eat:
    def __init__(self, x, z, eat):
        self.x, self.z = x, z
        self.eat = eat

class Filling_Eat(Base_Eat):
    def __init__(self, x, z, eat):
        super().__init__(x, z, max(30, min(eat, 80)))

class Light_food(Base_Eat):
    def __init__(self, x, z, eat):
        super().__init__(x, z, max(3, min(eat, 25)))

# Виды яблок

class Apple_slice(Light_food):
    def __init__(self, x, z, eat=7):
        super().__init__(x, z, max(4, min(eat, 9)))
        
class Apple(Filling_Eat):
    def __init__(self, x, z, eat=30):
        super().__init__(x, z, max(25, min(eat, 40)))
