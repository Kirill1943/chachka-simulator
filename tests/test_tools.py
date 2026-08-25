import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Game.Gameplay_tools.SortTools import sort_objects as sort
from Game.Gameplay_tools.ScanTools import scan

def test_sorts(fixture_create_eat, fixture_create_potion, fixture_create_chachka):
    chachka = fixture_create_chachka()
    eat = fixture_create_eat(eat_level=10)
    potion = fixture_create_potion(effect_level=2)

    objects_list = [chachka, eat, potion]

    assert sort.sort_eat(objects_list) == [eat]
    assert sort.sort_potions(objects_list) == [potion]
    assert set(sort.remove_chaks(objects_list)) == {eat, potion}

def test_dont_fail_scan(fixture_create_chachka, fixture_create_map, fixture_create_eat):
    Map = fixture_create_map(x1=-5, x2=5, z1=-5, z2=5)
    chachka = fixture_create_chachka()

    eat = fixture_create_eat(eat_level=20)
    Map.link_eat(eat)

    assert scan.scan_map(Map, 3, chachka.x, chachka.z) == [eat]