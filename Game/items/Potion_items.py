import os
import sys
import typing

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from effects import baffes

if typing.TYPE_CHECKING:
    from Chachka import Chachka

class potion:
    def __init__(self, effect_level, x, z):
        self.level = effect_level
        self.effect = ""
        self.x, self.z = x, z
    def use(self, chachka_object: Chachka):
        pass

class instant_regenerate_potion(potion):
    def __init__(self, effect_level, x, z):
        super().__init__(max(1, min(effect_level, 5)), z, x)
        self.effect = baffes.InstantRegeneration(self.level)
    def use(self, chachka_object: Chachka):
        hp = chachka_object.hp
        hp += self.effect.hp_regenerate
        chachka_object.hp = max(0, min(hp, 100))