import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from game.Gameplay.Map.gen_map import basegen, eazygen, hardgen
from game.Gameplay.Map.maps import Map


def regeneration(map_: Map, mode: str = "1"):
    mode = str(mode)

    only_chachka = []
    for i in map_.objects:
        if i.__class__.__name__ == "Chachka":
            only_chachka.append(i)
    map_.objects = only_chachka

    if hasattr(map_, 'eat') and isinstance(map_.eat, list):
        map_.eat = []

    if mode == "-1":
        hardgen(map_)
    elif mode == "0":
        basegen(map_)
    elif mode == "1":
        eazygen(map_)
    else:
        basegen(map_)
