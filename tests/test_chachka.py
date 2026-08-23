

def test_chachka_eating(fixture_create_chachka):
    chachka = fixture_create_chachka()
    chachka.eat = 15
    chachka.speed_eating(50)

    assert chachka.eat == 65

def test_chachka_death(fixture_create_chachka):
    chachka = fixture_create_chachka()
    chachka.hp = 0
    chachka.alive = False

    assert chachka.Viy(scream=3) is None
    assert chachka.Scream(scream=10) is None
    assert chachka.use_potions(radius=1) is None
    assert chachka.eating(radius=1) is None
    assert chachka.step(x=1, z=1) is None
    assert chachka.set_size([2, 2, 2]) is None

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

def test_chachka_map_borders(fixture_create_chachka, fixture_create_map):
    chachka = fixture_create_chachka()
    create_map = fixture_create_map(x1=-3, x2=3, z1=-3, z2=3)
    chachka.in_map = create_map

    chachka.x = 3
    chachka.z = 3

    chachka.step(3, 3)
    chachka.step(1, 1)

    assert chachka.x == 3
    assert chachka.z == 3