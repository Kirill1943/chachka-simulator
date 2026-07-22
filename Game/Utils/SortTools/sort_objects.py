import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Game.items.Eat_items import Base_Eat

def sort_eat(objects: list):
    eat = []
    for i in objects:
        if isinstance(i, Base_Eat):
            eat.append(i)
    return eat

def remove_chaks(objects: list):
    from Game.Chachka import Chachka
    result = objects.copy()
    for i in objects:
        if isinstance(i, Chachka):
            result.remove(i)
    return result