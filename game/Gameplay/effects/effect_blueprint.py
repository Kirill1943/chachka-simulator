# основа / чертежи для эффектов

class Effect:
    def __init__(self, level: int):
        self.effect = ""  # название эффекта
        self.type_effect = 0  # тип эффекта. -1 отрицательный. 0 нейтральный. 1 положительный
        self.level = level  # уровень эффекта

    def __str__(self):
        return f"Эффект {self.effect} Уровень {self.level}"

class BuffEffect(Effect):
    def __init__(self, effect: str, level: int):
        super().__init__(level)
        self.effect = effect
        self.type_effect = 1

class NeutralEffect(Effect):
    def __init__(self, effect: str, level: int):
        super().__init__(level)
        self.effect = effect
        self.type_effect = 0

class DebuffEffect(Effect):
    def __init__(self, effect: str, level: int):
        super().__init__(level)
        self.effect = effect
        self.type_effect = -1