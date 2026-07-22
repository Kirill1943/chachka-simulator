import os
import sys
from typing import Any

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Game.Chachka import Chachka


def run(Chack: Chachka):
    print("=== ЧИТЫ ===")
    while True:
        try:
            print("[Изменить HP] set_hp, hp_set")
            print("[ Нажмите Ctrl + C или введите exit для выхода из меню читов]")
            cmd = input().strip().lower()
            if cmd == "exit": 
                break
            if cmd in ["set_hp", "hp_set"]:
                hp: Any = input("Введите количество hp (от 0 до 100)")
                try:
                    hp = int(hp)
                except (ValueError, TypeError):
                    print('Некорректное количество HP, HP чачки остается прежним')
                else:
                    Chack.hp = hp
        except KeyboardInterrupt:
            print('Выход...')
            break