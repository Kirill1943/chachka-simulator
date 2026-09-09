import pytest


@pytest.mark.gameplay
def test_chachka_eating(fixture_create_chachka, fixture_create_map, fixture_create_eat):
    chachka = fixture_create_chachka()
    chachka.eat = 85
    created_map = fixture_create_map(x1=-3, x2=3, z1=-3, z2=3)
    chachka.in_map = created_map

    created_map.link_eat(fixture_create_eat(10, 1, 1))
    created_map.link_eat(fixture_create_eat(10, -1, -1))

    chachka.eating()

    assert len(created_map.eat) == 1
    assert chachka.eat == 95

@pytest.mark.gameplay
def test_chachka_death(fixture_create_chachka):
    chachka = fixture_create_chachka()
    chachka.hp = 0
    chachka.alive = False

    assert chachka.viy(scream=3) is None
    assert chachka.scream(scream=10) is None
    assert chachka.use_potions(radius=1) is None
    assert chachka.eating(radius=1) is None
    assert chachka.step(x=1, z=1) is None
    assert chachka.set_size([2, 2, 2]) is None

@pytest.mark.gameplay
def test_chachka_use_potions(fixture_create_chachka, fixture_create_potion, fixture_create_map):
    chachka = fixture_create_chachka()
    chachka.x = 1
    chachka.z = 1
    chachka.hp = 90
    potion = fixture_create_potion(effect_level=1)
    created_map = fixture_create_map(x1=-3, x2=3, z1=-3, z2=3)

    created_map.link_chack(chachka)
    created_map.link_potion(potion)

    chachka.use_potions()

    assert len(created_map.potions) == 0
    assert len(created_map.objects) == 1

@pytest.mark.gameplay
def test_chachka_overuse(fixture_create_chachka, fixture_create_map):
    chachka = fixture_create_chachka()
    chachka.stamina = 2
    chachka.hp = 100
    chachka.alive = True

    create_map = fixture_create_map(x1=-10, x2=10, z1=-10, z2=10)
    chachka.in_map = create_map

    chachka.step(3, 3)

    assert chachka.stamina == 0
    assert chachka.hp < 100
    assert chachka.alive is True

@pytest.mark.gameplay
def test_chachka_step_borders(fixture_create_chachka, fixture_create_map):
    chachka = fixture_create_chachka()
    create_map = fixture_create_map(x1=-3, x2=3, z1=-3, z2=3)
    chachka.in_map = create_map

    chachka.x = 3
    chachka.z = 3

    chachka.step(3, 3)
    chachka.step(1, 1)

    assert chachka.x == 3
    assert chachka.z == 3