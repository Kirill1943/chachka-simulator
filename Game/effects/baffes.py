from effect_blueprint import Buff_Effect as Buff

"""
положительные эффекты
"""

# моментальная регенерация (класс эффекта и уровни эффекта)

class instant_regeneration(Buff):
    def __init__(self, level: int):
        super().__init__(effect="regen", level=max(1, min(level, 5)))
        self.hp_regenerate = ...

class instant_regeneration_I(instant_regeneration):
    def __init__(self):
        super().__init__(level=1)
        self.hp_regenerate = 7

class instant_regeneration_II(instant_regeneration):
    def __init__(self):
        super().__init__(level=2)
        self.hp_regenerate = 16

class instant_regeneration_III(instant_regeneration):
    def __init__(self):
        super().__init__(level=3)
        self.hp_regenerate = 27

class instant_regeneration_IV(instant_regeneration):
    def __init__(self):
        super().__init__(level=4)
        self.hp_regenerate = 43

class instant_regeneration_V(instant_regeneration):
    def __init__(self):
        super().__init__(level=5)
        self.hp_regenerate = 64