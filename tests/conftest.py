import os
import sys

import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Game.Chachka import Chachka
from Game.Gameplay.items.Eat_items import Base_Eat
from Game.Gameplay.items.Potion_items import potion
from Game.Gameplay.Map.maps import Map


@pytest.fixture
def fixture_create_chachka():
    def _make_chachka():
        chachka = Chachka(age=0, x=0, z=0)
        chachka.hp = 100
        chachka.eat = 100
        chachka.stamina = 100
        return chachka
    return _make_chachka

@pytest.fixture
def fixture_create_map():
    def _make_map(x1, x2, z1, z2):
        return Map(x1, x2, z1, z2)
    return _make_map

@pytest.fixture
def fixture_create_eat():
    def _make_eat(eat_level: int, x: int = 0, z: int = 0):
        return Base_Eat(x=x, z=z, eat=eat_level)
    return _make_eat

@pytest.fixture
def fixture_create_potion():
    def _make_potion(effect_level: int, x: int = 0, z: int = 0):
        return potion(effect_level=effect_level, x=z, z=z)
    return _make_potion