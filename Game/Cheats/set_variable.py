import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Game.game import ClassGame


def set_ticks(ticks: int, game_class: ClassGame):
    try:
        ticks = int(ticks)
    except (ValueError, TypeError):
        pass
    game_class.ticks_passed = ticks