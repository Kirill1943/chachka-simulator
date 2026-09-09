import pytest

from game.Gameplay_tools.ScanTools import scan
from game.Gameplay_tools.SortTools import sort_objects as sort


@pytest.mark.utils
def test_sorts(fixture_create_eat, fixture_create_potion, fixture_create_chachka):
    chachka = fixture_create_chachka()
    eat = fixture_create_eat(eat_level=10)
    potion = fixture_create_potion(effect_level=2)

    objects_list = [chachka, eat, potion]

    assert sort.sort_eat(objects_list) == [eat]
    assert sort.sort_potions(objects_list) == [potion]
    assert set(sort.remove_chaks(objects_list)) == {eat, potion}

@pytest.mark.utils
def test_scan(fixture_create_chachka, fixture_create_map, fixture_create_eat):
    map_ = fixture_create_map(x1=-5, x2=5, z1=-5, z2=5)
    chachka = fixture_create_chachka()

    eat = fixture_create_eat(eat_level=20)
    map_.link_eat(eat)

    assert scan.scan_map(map_, 3, chachka.x, chachka.z) == [eat]

@pytest.mark.utils
@pytest.mark.input_invalid_values
def test_scan_with_invalid_value(fixture_create_chachka, fixture_create_map, fixture_create_eat):
    map_ = fixture_create_map(x1=-5, x2=5, z1=-5, z2=5)
    chachka = fixture_create_chachka()

    eat = fixture_create_eat(eat_level=20)
    map_.link_eat(eat)

    assert scan.scan_map(map_, "str", chachka.x, chachka.z) == [eat]