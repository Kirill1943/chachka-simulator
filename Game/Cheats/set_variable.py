import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Game.Chachka import Chachka
from Game.game import ClassGame


def set_ticks(ticks: int, game_class: ClassGame):
    try:
        ticks = int(ticks)
    except (ValueError, TypeError):
        return
    game_class.ticks_passed = ticks

def set_chachka_hp(hp: int, chachka: Chachka):
    try:
        hp = int(hp)
    except (ValueError, TypeError):
        return
    chachka.hp = max(0, min(hp, 100))

def set_chachka_stamina(stamina: int, chachka: Chachka):
    try:
        stamina = int(stamina)
    except (ValueError, TypeError):
        return
    chachka.stamina = max(0, min(stamina, 100))

def set_chachka_eat(eat: int, chachka: Chachka):
    try:
        eat = int(eat)
    except (ValueError, TypeError):
        return
    chachka.eat = max(0, min(eat, 100))