import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from game.Gameplay.items.eat import BaseEat
from game.Gameplay.items.potions import Potion


def sort_eat(objects: list):
    eat = []
    for i in objects:
        if isinstance(i, BaseEat):
            eat.append(i)
    return eat

def sort_potions(objects: list):
    potion_ = []
    for i in objects:
        if isinstance(i, Potion):
            potion_.append(i)
    return potion_

def remove_chaks(objects: list):
    result = objects.copy()
    for i in result:
        if i.__class__.__name__ == "Chachka":
            result.remove(i)
    return result
