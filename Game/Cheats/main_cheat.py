import os
import subprocess
import sys
from typing import Any

from pick import pick

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Game import logging as Log
from Game.Chachka import Chachka
from Game.Cheats import map_cheats as cheat_map
from Game.Cheats import set_variable as cheat_set
from Game.Map.maps import Map


def run(Chack: Chachka, Map: Map, logging_file_path: str):
    while True:
        try:
            subprocess.run(['cls'] if os.name == 'nt' else ['clear'], shell=False)
            menu_title = "=== ЧИТЫ ==="
            options = [
                "[Изменить HP      ] set_hp, hp_set",
                "[Изменить сытость ] set_eat, eat_set",
                "[Изменить стамину ] set_stamina, stamina_set",
                "[Пере-реген. карты] regen_map, map_regen",
                "Выйти из меню читов (exit)"
            ]
            cmd_keys = ["set_hp", "set_eat", "set_stamina", "regen_map", "exit"]
            
            option, index = pick(options, menu_title, indicator='=>')
            cmd = cmd_keys[index]
            
            if cmd == "exit": 
                break
            if cmd == "set_hp":
                Log.info(f'пользователь выбрал чит: {cmd} (изменение HP)', logging_file_path)
                hp: Any = input("Введите количество hp (от 0 до 100)")
                try:
                    hp = int(hp)
                except (ValueError, TypeError):
                    print('Некорректное количество HP, HP чачки остается прежним')
                else:
                    cheat_set.set_chachka_hp(hp, chachka=Chack)
                input("\nНажмите Enter для продолжения...")
            elif cmd == "set_eat":
                Log.info(f'пользователь выбрал чит: {cmd} (изменение сытости)', logging_file_path)
                eat: Any = input("Введите уровень сытости (от 0 до 100)")
                try:
                    eat = int(eat)
                except (ValueError, TypeError):
                    print('Некорректное количество сытости, сытость чачки остается прежним')
                else:
                    cheat_set.set_chachka_eat(eat, chachka=Chack)
                input("\nНажмите Enter для продолжения...")
            elif cmd == "set_stamina":
                Log.info(f'пользователь выбрал чит: {cmd} (изменение стамины)', logging_file_path)
                stamina: Any = input("Введите уровень стамины (от 0 до 100)")
                try:
                    stamina = int(stamina)
                except (ValueError, TypeError):
                    print('Некорректное количество стамины, стамина чачки остается прежним')
                else:
                    cheat_set.set_chachka_stamina(stamina, chachka=Chack)
                input("\nНажмите Enter для продолжения...")
            elif cmd == "regen_map":
                Log.info(f'пользователь выбрал чит: {cmd} (перерегенерация карты)', logging_file_path)
                cheat_map.regeneration(Map, mode=str(Map.gen_type))
                input("\nНажмите Enter для продолжения...")

        except KeyboardInterrupt:
            print('Выход...')
            break
