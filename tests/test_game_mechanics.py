

def test_tick_and_add_map(fixture_create_game, fixture_create_map, fixture_create_chachka):
    Map = fixture_create_map(x1=-5, x2=5, z1=-5, z2=5)
    Game = fixture_create_game()
    Chachka = fixture_create_chachka()

    Map.link_chack(Chachka)
    Game.add_map(Map)

    Chachka.stamina = 98.0
    Game.tick()

    assert Game.ticks_passed == 2
    assert Chachka.eat == 99.7
    assert Chachka.stamina == 99.5