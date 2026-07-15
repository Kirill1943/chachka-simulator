import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from effects import baffes
from Chachka import Chachka

class instant_regenerate_potion:
    def __init__(self, effect_level):
        self.level = max(1, min(effect_level, 5))
        self.effect = baffes.InstantRegeneration(self.level)
    def use(self, chachka_object: Chachka):
        if isinstance(chachka_object, Chachka):
            hp = chachka_object.hp
            hp += self.effect.hp_regenerate
            chachka_object.hp = max(0, min(hp, 100))
        else:
            pass