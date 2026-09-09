import pytest


@pytest.mark.gameplay
def test_link_chachka(fixture_create_map, fixture_create_chachka):
    map_ = fixture_create_map(x1=-5, x2=5, z1=-5, z2=5)
    chachka = fixture_create_chachka()

    map_.link_chack(chachka)

    assert chachka in map_.objects
    assert chachka in map_.chaks
    assert map_.get_object(chachka.x, chachka.z) == chachka

@pytest.mark.gameplay
def test_link_eat(fixture_create_map, fixture_create_eat):
    map_ = fixture_create_map(x1=-5, x2=5, z1=-5, z2=5)
    eat = fixture_create_eat(x=0, z=0, eat_level=20)

    map_.link_eat(eat)

    assert eat in map_.objects
    assert eat in map_.eat
    assert map_.get_object(eat.x, eat.z) == eat

@pytest.mark.gameplay
def test_link_potion(fixture_create_map, fixture_create_potion):
    map_ = fixture_create_map(x1=-5, x2=5, z1=-5, z2=5)
    potion_ = fixture_create_potion(x=0, z=0, effect_level=3)

    map_.link_potion(potion_)

    assert potion_ in map_.objects
    assert potion_ in map_.potions
    assert map_.get_object(potion_.x, potion_.z) == potion_

def test_get_object(fixture_create_chachka, fixture_create_map):
    map_ = fixture_create_map(x1=-5, x2=5, z1=-5, z2=5)
    chachka = fixture_create_chachka()

    chachka.x = 3
    chachka.z = 1

    map_.link_chack(chachka)

    assert map_.get_object(6, -9) == None
    assert map_.get_object(3, 1) == chachka