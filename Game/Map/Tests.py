import sys
import os.path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Chachka import Chachka

"""
тестовые карты
"""

class Map:
    def __init__(self, x1, x2, z1, z2):
        self.x1, self.x2 = x1, x2
        self.z1, self.z2 = z1, z2
        self.objects = []
        self.chaks = set([])
    def link_chack(self, chachka: Chachka):
        if isinstance(chachka, Chachka):
            chack_x = max(self.x1, min(chachka.x, self.x2))
            chack_z = max(self.z1, min(chachka.z, self.z2))
            chachka.x, chachka.z = chack_x, chack_z
            self.objects.append({
                "x": chack_x,
                "z": chack_z,
                "obj": chachka
            })