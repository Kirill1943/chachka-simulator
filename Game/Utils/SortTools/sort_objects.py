import os
import sys
import typing

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Game.items.Eat_items import Base_Eat


def sort_eat(objects: list):
    eat = []
    for i in objects:
        if isinstance(i, Base_Eat):
            eat.append(i)
    return eat

def sort_potions(objects: list):
    from Game.items.Potion_items import potion
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