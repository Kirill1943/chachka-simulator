

def test_tick_and_add_map(fixture_create_game, fixture_create_map, fixture_create_chachka):
    map_ = fixture_create_map(x1=-5, x2=5, z1=-5, z2=5)
    game = fixture_create_game()
    chachka = fixture_create_chachka()

    map_.link_chack(chachka)
    game.add_map(map_)

    chachka.stamina = 98.0
    game.tick()

    assert game.ticks_passed == 2
    assert chachka.eat == 99.7
    assert chachka.stamina == 99.5