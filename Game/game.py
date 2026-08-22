from Game.chachka_reanimation import reanim
from Game.Gameplay.Map.maps import Map


class ClassGame:
    def __init__(self, time: int = 1):
        self.maps: list[Map] = []
        self.time = time # как быстро будет течь время
        self.ticks_passed = time
    def tick(self):
        for map in self.maps:
            for chack in map.chaks:
                chack.stamina += 1.5
                chack.eat -= 0.3
                chack.age += self.time / 100
                
                if chack.eat < 0:
                    hp_spent = abs(chack.eat) / 5
                    chack.hp -= hp_spent
                
                if chack.hp <= 0:
                    chack.alive = False
                    print("Чачка умирает! начинаем реанимирование...")
                    chack.hp = 0
                    print("------")
                    reanim(chack)
                
                self.fix(chack)
                
        self.ticks_passed += self.time
    def fix(self, chack):
        """
        функция нужна для исправления значений переменных заданной чачки
        """
        chack.hp = max(0, min(chack.hp, 100))
        chack.eat = max(0, min(chack.eat, 100))
        chack.stamina = max(0, min(chack.stamina, 100))
    def add_map(self, map: Map):
        self.maps.append(map)