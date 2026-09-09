import os
import sys
from collections.abc import Callable
from typing import Any

import rich
from pick import pick

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from game import logging as log
from game.chachka import Chachka
from game.Cheats import chachka_cheats as cheat_set
from game.Cheats import map_cheats as cheat_map
from game.Gameplay.Map.maps import Map


def hp_set(chack, logging_file_path, **k):
    log.info('пользователь выбрал чит: изменение HP', logging_file_path)
    hp = input("Введите количество hp (от 0 до 100): ")
    try:
        hp = int(hp)
    except (ValueError, TypeError):
        print('Некорректное количество HP, HP чачки остается прежним')
    else:
        cheat_set.set_chachka_hp(hp, chachka=chack)
    input("\nНажмите Enter для продолжения...")

def eat_set(chack, logging_file_path, **k):
    log.info('пользователь выбрал чит: изменение сытости', logging_file_path)
    eat = input("Введите уровень сытости (от 0 до 100): ")
    try:
        eat = int(eat)
    except (ValueError, TypeError):
        print('Некорректное количество сытости, сытость чачки остается прежним')
    else:
        cheat_set.set_chachka_eat(eat, chachka=chack)
    input("\nНажмите Enter для продолжения...")

def stamina_set(chack, logging_file_path, **k):
    log.info('пользователь выбрал чит: изменение стамины', logging_file_path)
    stamina = input("Введите уровень стамины (от 0 до 100): ")
    try:
        stamina = int(stamina)
    except (ValueError, TypeError):
        print('Некорректное количество стамины, стамина чачки остается прежним')
    else:
        cheat_set.set_chachka_stamina(stamina, chachka=chack)
    input("\nНажмите Enter для продолжения...")

def regen_map(logging_file_path, map_: Map, **k):
    log.info('пользователь выбрал чит: перерегенерация карты', logging_file_path)
    cheat_map.regeneration(map_, mode=str(Map.gen_type))
    input("\nНажмите Enter для продолжения...")

def set_immortality(logging_file_path: str, cheat_conf: str, **k):
    menu_title = "--- Выберите вариант ---"
    options = [
        "Включить бессмертие",
        "Выключить бессмертие"
    ]
    cmd_keys = [True, False]
    option, index = pick(options, menu_title, indicator='=>')

    key = cmd_keys[index]
    cheat_set.set_chachka_immortality(key, cheat_conf, logging_file_path)

    rich.print("[#FFFF00]ПРЕДУПРЕЖДЕНИЕ! необходимо перезапустить игру чтобы настройки применились")
    input("\nНажмите Enter для продолжения...")

COMMANDS: dict[str, Callable[..., Any]] = {
    "set_hp": hp_set, 
    "set_eat": eat_set,
    "set_stamina": stamina_set,
    "regen_map": regen_map,
    "immortality": set_immortality
}

def run(chack: Chachka, map_: Map, logging_file_path: str, config_path: str):
    while True:
        try:
            print("\033[H\033[J", end="")
            menu_title = "=== ЧИТЫ ==="
            options = [
                "[Изменить HP]",
                "[Изменить сытость]",
                "[Изменить стамину]",
                "[Регенерация карты]",
                "[Включить / Выключить бессмертие]",
                "[Выход]"
            ]
            cmd_keys = ["set_hp", "set_eat", "set_stamina", "regen_map", "immortality", "exit"]
            
            option, index = pick(options, menu_title, indicator='=>')
            cmd = cmd_keys[index]
            
            if cmd == "exit":
                break
            else:
                COMMANDS[cmd](Chack=chack, logging_file_path=logging_file_path, map_=map_, cheat_conf=config_path)

        except KeyboardInterrupt:
            print('Выход...')
            break
