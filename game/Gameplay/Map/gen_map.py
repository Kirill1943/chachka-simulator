import os
import secrets
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from game.Gameplay.items import eat, potions
from game.Gameplay.Map import maps


def hardgen(map_: maps.Map):
    """
    сложная генерация, непросто выжить
    """
    if isinstance(map_, maps.Map):
        x1, x2 = min(map_.x1, map_.x2), max(map_.x1, map_.x2)
        z1, z2 = min(map_.z1, map_.z2), max(map_.z1, map_.z2)

        occupied_coords = set([])
        for i in map_.objects:
            occupied_coords.add((i.x, i.z))
        for x in range(x1, x2 + 1):
            for z in range(z1, z2 + 1):
                if (x, z) in occupied_coords:
                    continue
                choice = secrets.randbelow(100) + 1
                if 1 <= choice <= 3:
                    map_.link_eat(eat.Apple(x=x, z=z))
                elif 4 <= choice <= 25:
                    map_.link_eat(eat.AppleSlice(x=x, z=z))
                else:
                    continue
        map_.gen_type = -1

def basegen(map_: maps.Map):
    """
    базовая генерация карты. легко выжить
    """
    if isinstance(map_, maps.Map):
        x1, x2 = min(map_.x1, map_.x2), max(map_.x1, map_.x2)
        z1, z2 = min(map_.z1, map_.z2), max(map_.z1, map_.z2)

        occupied_coords = set([])
        for i in map_.objects:
            occupied_coords.add((i.x, i.z))
        for x in range(x1, x2 + 1):
            for z in range(z1, z2 + 1):
                if (x, z) in occupied_coords:
                    continue
                choice = secrets.randbelow(100) + 1
                if 1 <= choice <= 2:
                    map_.link_potion(potions.InstantRegeneratePotion(effect_level=2, x=x, z=z))
                elif 3 <= choice <= 10:
                    map_.link_eat(eat.Apple(x=x, z=z))
                elif 11 <= choice <= 36:
                    map_.link_eat(eat.AppleSlice(x=x, z=z))
                else:
                    continue
        map_.gen_type = 0

def eazygen(map_: maps.Map):
    """
    легкая генерация карты. почти невозможно умереть
    """
    if isinstance(map_, maps.Map):
        x1, x2 = min(map_.x1, map_.x2), max(map_.x1, map_.x2)
        z1, z2 = min(map_.z1, map_.z2), max(map_.z1, map_.z2)

        occupied_coords = set([])
        for i in map_.objects:
            occupied_coords.add((i.x, i.z))
        for x in range(x1, x2 + 1):
            for z in range(z1, z2 + 1):
                if (x, z) in occupied_coords:
                    continue
                choice = secrets.randbelow(100) + 1
                if 1 <= choice <= 70:
                    map_.link_eat(eat.Apple(x=x, z=z, eat=40))
                elif 71 <= choice <= 72:
                    map_.link_potion(potions.InstantRegeneratePotion(effect_level=1, x=x, z=z))
                elif 73 <= choice <= 75:
                    map_.link_potion(potions.InstantRegeneratePotion(effect_level=2, x=x, z=z))
                elif 76 <= choice <= 80:
                    map_.link_potion(potions.InstantRegeneratePotion(effect_level=3, x=x, z=z))
                elif 81 <= choice <= 88:
                    map_.link_potion(potions.InstantRegeneratePotion(effect_level=4, x=x, z=z))
                elif 89 <= choice <= 92:
                    map_.link_potion(potions.InstantRegeneratePotion(effect_level=5, x=x, z=z))
                else:
                    continue
        map_.gen_type = 1