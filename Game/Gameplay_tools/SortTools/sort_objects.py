import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Game.Gameplay.items.Eat_items import Base_Eat
from Game.Gameplay.items.Potion_items import potion


def sort_eat(objects: list):
    eat = []
    for i in objects:
        if isinstance(i, Base_Eat):
            eat.append(i)
    return eat

def sort_potions(objects: list):
    potion_ = []
    for i in objects:
        if isinstance(i, potion):
            potion_.append(i)
    return potion_

def remove_chaks(objects: list):
    result = objects.copy()
    for i in result:
        if i.__class__.__name__ == "Chachka":
            result.remove(i)
    return result
