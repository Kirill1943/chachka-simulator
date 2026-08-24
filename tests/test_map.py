

def test_link_chachka(fixture_create_map, fixture_create_chachka):
    Map = fixture_create_map(x1=-5, x2=5, z1=-5, z2=5)
    Chachka = fixture_create_chachka()

    Map.link_chack(Chachka)

    assert Chachka in Map.objects
    assert Chachka in Map.chaks
    assert Map.get_object(Chachka.x, Chachka.z) == Chachka

def test_link_eat(fixture_create_map, fixture_create_eat):
    Map = fixture_create_map(x1=-5, x2=5, z1=-5, z2=5)
    Eat = fixture_create_eat(eat_count=20)

    Map.link_eat(Eat)

    assert Eat in Map.objects
    assert Eat in Map.eat
    assert Map.get_object(Eat.x, Eat.z) == Eat