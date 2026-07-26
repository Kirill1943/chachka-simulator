import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Game.effects.effect_blueprint import Buff_Effect as Buff

"""
положительные эффекты
"""

# Моментальная регенерация (Класс эффекта и уровни 1-5)

class InstantRegeneration(Buff):
    def __init__(self, level: int):
        self.effect = "Regen"
        self.level = max(1, min(level, 5))
        
        hp_values = {
            1: 8,
            2: 14,
            3: 29,
            4: 41,
            5: 65
        }
        
        self.hp_regenerate = hp_values[self.level]