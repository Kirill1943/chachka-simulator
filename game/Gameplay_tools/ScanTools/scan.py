import os
import sys

import rich

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from game.Gameplay.Map.maps import Map


def scan_map(map_: Map, distance: int, chachka_x: int, chachka_z: int):
    try:
        distance = int(distance)
    except (ValueError, TypeError):
        distance = 3
        rich.print('[#FFFF00][WARNING][/] Дистанция не указана как число, выбрано стандартное число: 3')
    objects = []
    for x in range(chachka_x - distance, chachka_x + distance + 1):
        for z in range(chachka_z - distance, chachka_z + distance + 1):
            if map_.x1 <= x <= map_.x2 and map_.z1 <= z <= map_.z2:
                obj = map_.get_object(x, z)
                if obj is not None:
                    objects.append(obj)
    return objects