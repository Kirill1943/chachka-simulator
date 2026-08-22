import json
import os
import sys
from datetime import datetime
from typing import Any

import rich
from pick import pick

from Game import Chachka
from Game import logging as GameLog
from Game.Cheats import main_cheat as cheat
from Game.game import ClassGame
from Game.Gameplay.Map import gen_map, maps
from Game.UI.GUI import drawing_map as draw_map

CONFIG_PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Config"))

with open(os.path.join(CONFIG_PATH, "Game.json"), "r", encoding="utf-8") as file:
    GAME_CONFIG = json.load(file)

now = datetime.now()

raw_log_path = os.path.join(*(GAME_CONFIG["Logging"]["LogPath"]))

log_path = str(raw_log_path).format(Day=now.strftime("%d"), Month=now.strftime("%m"), Year=now.strftime("%Y"))

os.makedirs(os.path.dirname(log_path), exist_ok=True)
if not os.path.exists(log_path): 
    open(log_path, "w", encoding="utf-8").close()
else: 
    with open(log_path, "a", encoding="utf-8") as file:
        file.write("-----\n")
if len(sys.argv) > 1 and sys.argv[1] == "--cheats":
    CHEATS = True
else:
    CHEATS = False


def command_info(pet: Chachka.Chachka, Gameclass: ClassGame, **k):
    GameLog.info("Пользователь Ввел команду информации об чачке (info)", log_path)
    print("==== ИНФОРМАЦИЯ ОБ ЧАЧКЕ ====")
    status = "здоровая" if pet.hp >= 80 else "несильно повреждена" if pet.hp >= 60 else "повреждена" if pet.hp >= 20 else "критически повреждена" if pet.hp >= 5 else "почти умерла"
    print(f"Хп: {pet.hp}, Статус: {status}")
    print(f"Голод: {pet.eat}")
    print(f"Жива: {'Да' if pet.alive else 'Нет'}")
    print(f"Выносливость: {pet.stamina}")
    print(f"прошло тиков времени: {Gameclass.ticks_passed}")
    print(f"Координаты чачки: X: {pet.x}, Z: {pet.z}")
    print("=============================")
    input("\nНажмите Enter, чтобы вернуться в меню...")

def command_eat(pet: Chachka.Chachka, **k):
    GameLog.info("Пользователь Ввел команду поедания (eat)", log_path)
    print('чачка ест...')
    pet.eating()
    input("\nНажмите Enter, чтобы вернуться в меню...")

def command_step(pet: Chachka.Chachka, **k):
    GameLog.info("Пользователь Ввел команду передвижения (step)", log_path)
    x: Any = input("введите насколько передвинуться чачке по X: ")
    z: Any = input("введите насколько передвинуться чачке по Z: ")
    try:
        x, z = int(x), int(z)
    except (ValueError, TypeError):
        print('некоректные координаты')
        return
    pet.step(x, z)
    input("\nНажмите Enter, чтобы вернуться в меню...")

def command_cheat(pet: Chachka.Chachka, map: maps.Map, conf_path: str, **k):
    GameLog.info("Пользователь открывает читы...", log_path)
    if CHEATS:
        print("===========================")
        cheat.run(Chack=pet, Map=map, logging_file_path=log_path, config_path=conf_path)
        print("===========================")
        input("\nНажмите Enter, чтобы вернуться в меню...")
    else:
        rich.print('[#FF0000] ERROR: Доступ запрещен - читы не включены')
        GameLog.access_denied('Пользователь попытался войти в вкладку читов но запустил игру без этой возможности', log_path)
        input("\nНажмите Enter, чтобы вернуться в меню...")

def command_drawmap(map: maps.Map, **k):
    GameLog.info("Пользователь Ввел команду отрисовки карты (drawmap)", log_path)
    draw_map.draw(map)
    input("\nНажмите Enter, чтобы вернуться в меню...")

def command_use_potions(pet: Chachka.Chachka, **k):
    GameLog.info("Пользователь Ввел команду поглощения зелей (use_potion / s)", log_path)
    pet.use_potions()
    input("\nНажмите Enter, чтобы вернуться в меню...")

def Null_Method(**k):
    pass

COMMANDS = {
    "info": command_info,
    "eat": command_eat,
    "step": command_step,
    "cheat": command_cheat,
    "cheats": command_cheat,
    "drawmap": command_drawmap,
    "use_potion": command_use_potions,
    "use_potions": command_use_potions,
    "": Null_Method
}

def run():
    menu_title = "Выберите генерацию игры:"
    options = [
        "-1. сложная генерация",
        "0. стандартная регенерация (по умолчанию)",
        "1. легкая генерация"
    ]
    keys = ["-1", "0", "1"]
    option, index = pick(options, menu_title, indicator='=>')
    generate_type = keys[index]

    if generate_type not in ["-1", "0", "1"]:
        generate_type = "0"

    if generate_type == "-1":
        generate_type_txt = "сложно"
    elif generate_type == "0":
        generate_type_txt = "стандарт"
    elif generate_type == "1":
        generate_type_txt = "легкий"

    GameLog.info(f"Игра запущена, Выбран режим игры: {generate_type_txt}", log_path)

    if CHEATS: 
        rich.print('[#FFBB00][WARNING][/] Читы включены')
        GameLog.warning("Читы включены", log_path)

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

    cheat_config = os.path.abspath(os.path.join("Config", "Cheats.json"))
    while True:
        print("\033[H\033[J", end="")
        menu_title = f"=== Симулятор Чачки ===\nХп: {round(pet.hp, 1)} | Сытость: {round(pet.eat, 1)} | Выносливость: {pet.stamina}\nКоординаты: X: {pet.x}, Z: {pet.z}\nВыберите действие:"
        
        options = [
            'Пропустить ход',
            'Информация об чачке (info)',
            'Отрисовать карту (drawmap)',
            'Есть все что вокруг (eat)',
            'Сделать шаг (step)',
            'Выпить зелья в радиусе 1 клетки (Use_potion / Use_potions)',
            'крикнуть / викнуть'
        ]
        
        cmd_keys = ['', 'info', 'drawmap', 'eat', 'step', 'use_potions', 'viy']
        
        if CHEATS:
            options.append('Открыть чит-меню (Cheat)')
            cmd_keys.append('cheat')

        options.append('Выйти из игры (Exit)')
        cmd_keys.append('exit')
        
        _, index = pick(options, menu_title, indicator='=>')
        
        cmd_key = cmd_keys[index]
        
        if cmd_key == 'exit':
            GameLog.info('Игра завершена пользователем', log_path)
            break
        elif cmd_key == 'viy':
            menu_title = "=== Выберите тип ==="
            GameLog.info('пользователь выполнил команду ора чачки (viy / scream)', log_path)
            text_options = [
                'тихо викнуть',
                'заорать'
            ]
            key_options = ["vi", "scream"]
            _, index = pick(text_options, menu_title, indicator='=>')
            option = key_options[index]
            if option == "vi":
                scream = input("насколько громко викнуть чачке? (от 1 до 5): ")
                try:
                    scream = max(1, min(5, int(scream)))
                except (ValueError, TypeError):
                    print("неверное значение")
                    continue
                pet.Viy(scream)
            elif option == "scream":
                scream = input("насколько громко заорать чачке? (от 8 до 15): ")
                try:
                    scream = max(8, min(15, int(scream)))
                except (ValueError, TypeError):
                    print("неверное значение")
                    continue
                pet.Scream(scream)

            input("\nНажмите Enter, чтобы вернуться в меню...")
        else:
            COMMANDS[cmd_key](pet=pet, Gameclass=Gameclass, map=map_game, conf_path=cheat_config)
                
        Gameclass.tick()


if __name__ == "__main__":
    run()
