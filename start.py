import datetime
import json
import os
import sys
from typing import Any

import rich

from Game import Chachka
from Game import logging as GameLog
from Game.Cheats import main_cheat as cheat
from Game.game import ClassGame
from Game.Map import gen_map, maps
from Game.UI import drawing_map_GUI as draw_map

CONFIG_PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Config"))

with open(os.path.join(CONFIG_PATH, "Game.json"), "r", encoding="utf-8") as file:
    GAME_CONFIG = json.load(file)

now = datetime.datetime.now()

raw_log_path = os.path.join(*(GAME_CONFIG["Logging"]["LogPath"]))

log_path = str(raw_log_path).format(Day=now.strftime("%d"), Month=now.strftime("%m"), Year=now.strftime("%Y"))

os.makedirs(os.path.dirname(log_path), exist_ok=True)
if not os.path.exists(log_path): open(log_path, "w", encoding="utf-8").close()
else: open(log_path, "a", encoding="utf-8").write("-----\n")
if len(sys.argv) > 1 and sys.argv[1] == "--cheats":
    CHEATS = True
else:
    CHEATS = False


def command_info(pet: Chachka.Chachka, Gameclass: ClassGame, map: maps.Map):
    GameLog.info(f"Пользователь Ввел команду информации об чачке (info)", log_path)
    print(f"==== ИНФОРМАЦИЯ ОБ ЧАЧКЕ ====")
    status = "здоровая" if pet.hp >= 80 else "несильно повреждена" if pet.hp >= 60 else "повреждена" if pet.hp >= 20 else "критически повреждена" if pet.hp >= 5 else "почти умерла"
    print(f"Хп: {pet.hp}, Статус: {status}")
    print(f"Голод: {pet.eat}")
    print(f"Жива: {'Да' if pet.alive else 'Нет'}")
    print(f"Выносливость: {pet.stamina}")
    print(f"прошло тиков времени: {Gameclass.ticks_passed}")
    print(f"Координаты чачки: X: {pet.x}, Z: {pet.z}")
    print(f"=============================")

def command_eat(pet: Chachka.Chachka, Gameclass: ClassGame, map: maps.Map):
    GameLog.info(f"Пользователь Ввел команду поедания (eat)", log_path)
    print('чачка ест...')
    pet.eating()

def command_step(pet: Chachka.Chachka, Gameclass: ClassGame, map: maps.Map):
    GameLog.info(f"Пользователь Ввел команду передвижения (step)", log_path)
    x: Any = input("введите насколько передвинуться чачке по X: ")
    z: Any = input("введите насколько передвинуться чачке по Z: ")
    try:
        x, z = int(x), int(z)
    except (ValueError, TypeError):
        print('некоректные координаты')
        return
    pet.step(x, z)

def command_cheat(pet: Chachka.Chachka, Gameclass: ClassGame, map: maps.Map):
    GameLog.info(f"Пользователь открывает читы...", log_path)
    if CHEATS:
        print("===========================")
        cheat.run(Chack=pet, Map=map, logging_file_path=log_path)
        print("===========================")
    else:
        rich.print('[#FF0000] ERROR: Доступ запрещен - читы не включены')
        GameLog.access_denied('Пользователь попытался войти в вкладку читов но запустил игру без этой возможности', log_path)

def command_drawmap(pet: Chachka.Chachka, Gameclass: ClassGame, map: maps.Map):
    GameLog.info(f"Пользователь Ввел команду отрисовки карты (drawmap)", log_path)
    draw_map.draw(map)

COMMANDS = {
    "info": command_info,
    "eat": command_eat,
    "step": command_step,
    "cheat": command_cheat,
    "cheats": command_cheat,
    "drawmap": command_drawmap
}

def run():
    print('Выберите генерацию игры:')
    print("-1. сложная генерация")
    print('0. стандартная регенерация (по умолчанию)')
    print('1. легкая генерация')
    
    generate_type = input().strip()
    if generate_type not in ["-1", "0", "1"]:
        generate_type = "0"

    if generate_type == "-1":
        generate_type_txt = "сложно"
    elif generate_type == "0":
        generate_type_txt = "стандарт"
    elif generate_type == "1":
        generate_type_txt = "легкий"

    GameLog.info(f"Игра запущена, Выбран режим игры: {generate_type_txt}", log_path)

    print('=== Chachka Simulator - симулятор чачки ===')
    if CHEATS: 
        rich.print('[#FFBB00][WARNING][/] Читы включены')
        GameLog.warning(f"Читы включены", log_path)
    print('--- подготовка игры    ---')

    pet = Chachka.Chachka(age=0.5, x=0, z=0)
    map_game = maps.Map(x1=-5, x2=5, z1=-5, z2=5)
    map_game.link_chack(chachka=pet)

    if generate_type == "-1":
        gen_map.hardgen(map_game)
    elif generate_type == "0":
        gen_map.basegen(map_game)
    elif generate_type == "1":
        gen_map.eazygen(map_game)

    Gameclass = ClassGame()
    Gameclass.add_map(map_game)
    print('--- подготовка окончена ---')
    
    while True:
        print("---\nExit - выход,\nInfo - информация об чачке,\ndrawmap: отрисовать карту,\neat: есть все что вокруг\nStep - шаг\n---")
        print('введите действие: ')
        if CHEATS: 
            rich.print('[#AAFF00](Читы активированы, Введите Cheat для открытия читов)')
        
        cmd = input().strip().lower()
        
        if cmd in COMMANDS:
            COMMANDS[cmd](pet, Gameclass, map_game)
        elif cmd == "exit":
            break
        else:
            print('такой команды нету')
            GameLog.info('Пользователь ввел неверную команду', log_path)
        Gameclass.tick()


if __name__ == "__main__":
    run()
