import os
import sys

import rich

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Game.Map.maps import Map


def scan_map(Map: Map, distance: int):
    try:
        distance = int(distance)
    except (ValueError, TypeError):
        distance = 3
        rich.print('[#FFFF00][WARNING][/] Дистанция не указана как число, выбрано стандартное число: 3')
    objects = []
    for x in range(Map.x1 - distance, Map.x2 + distance + 1):
        for z in range(Map.z1 - distance, Map.z2 + distance + 1):
            obj = Map.get_object(x, z)
            if obj == None:
                pass
            else:
                objects.append(obj)
    return objects