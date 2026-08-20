import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Game.Gameplay.Map.gen_map import basegen, eazygen, hardgen
from Game.Gameplay.Map.maps import Map


def regeneration(Map: Map, mode: str = "1"):
    mode = str(mode)

    only_chachka = []
    for i in Map.objects:
        if i.__class__.__name__ == "Chachka":
            only_chachka.append(i)
    Map.objects = only_chachka

    if hasattr(Map, 'eat') and isinstance(Map.eat, list):
        Map.eat = []

    if mode == "-1":
        hardgen(Map)
    elif mode == "0":
        basegen(Map)
    elif mode == "1":
        eazygen(Map)
    else:
        basegen(Map)
