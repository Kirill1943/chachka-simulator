import os
import sys
from typing import Any

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Game.Chachka import Chachka
from Game.Cheats import map_cheats as cheat_map
from Game.Cheats import set_variable as cheat_set
from Game.Map.maps import Map


def run(Chack: Chachka, Map: Map):
    print("=== ЧИТЫ ===")
    while True:
        try:
            print("[Изменить HP      ] set_hp, hp_set")
            print("[Изменить сытость ] set_eat, eat_set")
            print("[Изменить стамину ] set_stamina, stamina_set")
            print("[Пере-реген. карты] regen_map, map_regen")
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
                    cheat_set.set_chachka_hp(hp, chachka=Chack)
            elif cmd in ["set_eat", "eat_set"]:
                eat: Any = input("Введите уровень сытости (от 0 до 100)")
                try:
                    eat = int(eat)
                except (ValueError, TypeError):
                    print('Некорректное количество сытости, сытость чачки остается прежним')
                else:
                    cheat_set.set_chachka_eat(eat, chachka=Chack)
            elif cmd in ["set_stamina", "stamina_set"]:
                stamina: Any = input("Введите уровень стамины (от 0 до 100)")
                try:
                    stamina = int(stamina)
                except (ValueError, TypeError):
                    print('Некорректное количество стамины, стамина чачки остается прежним')
                else:
                    cheat_set.set_chachka_stamina(stamina, chachka=Chack)
            elif cmd in ["regen_map", "map_regen"]:
                cheat_map.regeneration(Map, mode=str(Map.gen_type))

        except KeyboardInterrupt:
            print('Выход...')
            break