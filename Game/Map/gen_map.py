import os
import secrets
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Game.items import Eat_items as eat
from Game.Map import maps


def basegen(Map):
    """
    базовая генерация карты. легко выжить
    """
    if isinstance(Map, maps.Map):
        x1, x2 = min(Map.x1, Map.x2), max(Map.x1, Map.x2)
        z1, z2 = min(Map.z1, Map.z2), max(Map.z1, Map.z2)

        Occupied_Coords = set([])
        for i in Map.objects:
            Occupied_Coords.add((i.x, i.z))
        for x in range(x1, x2 + 1):
            for z in range(z1, z2 + 1):
                if (x, z) in Occupied_Coords:
                    continue
                choice = secrets.randbelow(100) + 1
                if 1 <= choice <= 7:
                    Map.link_eat(eat.Apple(x=x, z=z))
                elif 8 <= choice <= 33:
                    Map.link_eat(eat.Apple_slice(x=x, z=z))
                else:
                    continue
        Map.gen_type = 1

def eazygen(Map):
    """
    легкая генерация карты. почти невозможно умереть
    """
    if isinstance(Map, maps.Map):
        x1, x2 = min(Map.x1, Map.x2), max(Map.x1, Map.x2)
        z1, z2 = min(Map.z1, Map.z2), max(Map.z1, Map.z2)

        Occupied_Coords = set([])
        for i in Map.objects:
            Occupied_Coords.add((i.x, i.z))
        for x in range(x1, x2 + 1):
            for z in range(z1, z2 + 1):
                if (x, z) in Occupied_Coords:
                    continue
                choice = secrets.randbelow(100) + 1
                if 1 <= choice <= 90:
                    Map.link_eat(eat.Apple(x=x, z=z, eat=40))
                else:
                    continue
        Map.gen_type = 2