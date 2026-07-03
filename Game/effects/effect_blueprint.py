"""
основа / чертежи для эффектов
"""

class Effect:
    def __init__(self, level):
        self.effect = ... # название эффекта
        self.type_effect = ... # тип эффекта. -1 отрицательный. 0 нейтральный. 1 положительный
        self.level = level # уровень эффекта
    def __str__(self):
        return f"Эффект {self.effect} Уровень {self.level}"

class Buff_Effect(Effect):
    def __init__(self, effect, level):
        super().__init__(level)
        self.effect = effect
        self.type_effect = 1

class Neutral_Effect(Effect):
    def __init__(self, effect, level):
        super().__init__(level)
        self.effect = effect
        self.type_effect = 0

class Debuff_Effect(Effect):
    def __init__(self, effect, level):
        super().__init__(level)
        self.effect = effect
        self.type_effect = -1

Buff_Effect("", 1)