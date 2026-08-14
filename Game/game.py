from Game.chachka_reanimation import reanim
from Game.Map.maps import Map
from Game.Utils.cpp_utils.clamp import clamp_double as clamp


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
                if chack.hp <= 0:
                    chack.alive = False
                    print("Чачка умирает! начинаем реанимирование...")
                    chack.hp = 0
                    reanim(chack)
                if chack.eat < 0:
                    hp_spent = abs(chack.eat) / 5
                    print("Чачка истощена. ей нужно поесть иначе она начнет получать урон")
                    chack.hp -= hp_spent
                self.fix(chack)
        self.ticks_passed += self.time
    def fix(self, chack):
        """
        функция нужна для исправления значений переменных заданной чачки
        """
        chack.hp = clamp(0, chack.hp, 100)
        chack.eat = clamp(0, chack.eat, 100)
        chack.stamina = clamp(0, chack.stamina, 100)
    def add_map(self, map: Map):
        self.maps.append(map)