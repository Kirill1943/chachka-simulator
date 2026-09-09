

# типы еды (от которых идет наследование)

class BaseEat:
    def __init__(self, x, z, eat):
        self.x, self.z = x, z
        self.eat = eat

class FillingEat(BaseEat):
    def __init__(self, x, z, eat):
        super().__init__(x, z, max(30, min(eat, 80)))

class LightFood(BaseEat):
    def __init__(self, x, z, eat):
        super().__init__(x, z, max(3, min(eat, 25)))

# Виды яблок

class AppleSlice(LightFood):
    def __init__(self, x, z, eat=7):
        super().__init__(x, z, max(4, min(eat, 9)))
        
class Apple(FillingEat):
    def __init__(self, x, z, eat=30):
        super().__init__(x, z, max(25, min(eat, 40)))
