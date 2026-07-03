import os
import sys
import random

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Game.items import eat_items as eat
from Game.Map import maps

def basegen(Map):
    """
    базовая генерация карты. легко выжить
    """
    if isinstance(Map, maps.Map):
        x1, x2 = min(Map.x1, Map.x2), max(Map.x1, Map.x2)
        z1, z2 = min(Map.z1, Map.z2), max(Map.z1, Map.z2)

        for x in range(x1, x2 + 1):
            for z in range(z1, z2 + 1):
                choice = random.randint(1, 100)
                if 0 <= choice <= 7:
                    Map.link_eat(eat.Apple(x=x, z=z))
                elif 8 <= choice <= 33:
                    Map.link_eat(eat.Apple_slice(x=x, z=z))
                else:
                    continue
