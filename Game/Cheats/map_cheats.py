import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Game.Map.gen_map import basegen, eazygen
from Game.Map.maps import Map


def regeneration(Map: Map, mode: str = "1"):
    mode = str(mode)
    if mode == "1":
        basegen(Map)
    elif mode == "2":
        eazygen(Map)
    else:
        basegen(Map)