import os
import secrets
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from Game.Gameplay.items import Eat_items as eat
from Game.Gameplay.items import Potion_items as potions
from Game.Gameplay.Map import maps


def hardgen(Map: maps.Map):
    """
    сложная генерация, непросто выжить
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
                if 1 <= choice <= 3:
                    Map.link_eat(eat.Apple(x=x, z=z))
                elif 4 <= choice <= 25:
                    Map.link_eat(eat.Apple_slice(x=x, z=z))
                else:
                    continue
        Map.gen_type = -1

def basegen(Map: maps.Map):
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
                if 1 <= choice <= 2:
                    Map.link_potion(potions.instant_regenerate_potion(effect_level=2, x=x, z=z))
                elif 3 <= choice <= 10:
                    Map.link_eat(eat.Apple(x=x, z=z))
                elif 11 <= choice <= 36:
                    Map.link_eat(eat.Apple_slice(x=x, z=z))
                else:
                    continue
        Map.gen_type = 0

def eazygen(Map: maps.Map):
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
                if 1 <= choice <= 70:
                    Map.link_eat(eat.Apple(x=x, z=z, eat=40))
                elif 71 <= choice <= 72:
                    Map.link_potion(potions.instant_regenerate_potion(effect_level=1, x=x, z=z))
                elif 73 <= choice <= 75:
                    Map.link_potion(potions.instant_regenerate_potion(effect_level=2, x=x, z=z))
                elif 76 <= choice <= 80:
                    Map.link_potion(potions.instant_regenerate_potion(effect_level=3, x=x, z=z))
                elif 81 <= choice <= 88:
                    Map.link_potion(potions.instant_regenerate_potion(effect_level=4, x=x, z=z))
                elif 89 <= choice <= 92:
                    Map.link_potion(potions.instant_regenerate_potion(effect_level=5, x=x, z=z))
                else:
                    continue
        Map.gen_type = 1