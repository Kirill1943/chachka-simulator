import json
import os
import sys
from datetime import datetime
from typing import Any

import rich
from pick import pick

from game import chachka, saves
from game import logging as logs
from game.Cheats import main_cheat as cheat
from game.game import ClassGame
from game.Gameplay.Map import gen_map, maps
from game.ui.gui import drawing_map as draw_map

CONFIG_PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Config"))

with open(os.path.join(CONFIG_PATH, "game.json"), encoding="utf-8") as file:
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
CHEATS = len(sys.argv) > 1 and sys.argv[1] == "--cheats"


def load_chachka(pet: chachka.Chachka, map_: maps.Map, **k):
    target_dir = os.path.join(".", "saves")

    def _check_dir(filename):
        full_path = os.path.join(target_dir, filename)
        if os.path.isfile(full_path) and filename.endswith(".chachka_simulator.save"):
            return filename
        return None
    files = list(filter(None, map(_check_dir, os.listdir(target_dir))))

    keys = [*files]
    option, index = pick(files, title="--- Выберите файл сохранения из которого будет загружен питомец", indicator="->")
    key = keys[index]

    data_corrupted = False
    with open((filename := os.path.join(target_dir, key)), encoding="utf-8"):
        print("загрузка информации...")
        print("-----------------------")
        loaded_pet, date_time = saves.load(filename, map_)
        if loaded_pet is None:
            print("[ERROR] сохранение повреждено и не может быть восстановлено")
            data_corrupted = True
        else:
            date_time_parts = date_time.split() # type: ignore[union-attr]
            time = date_time_parts[1]
            date = date_time_parts[0]
            
            if time == "??:??:??": time = "[УТЕРЯНО]"
            if date == "XX.XX.XXXX": date = "[УТЕРЯНО]"
            print("=== ДАТА СОХРАНЕНИЯ ===")
            print(f"Время сохранения: {time}")
            print(f"Дата сохранения: {date}")
            print("=== О ПИТОМЦЕ ===")
            print(f"Здоровье: {loaded_pet.hp}")
            print(f"Сытость: {loaded_pet.eat}")
            print(f"Выносливость: {loaded_pet.stamina}")
            print(f"Возвраст: {loaded_pet.age}")
            print("=================")
            yes_or_no = input("Подвердить загрузку из сохранения? [Y/n]")
            if yes_or_no.lower().strip() in ["y", "н", "д"]:
                print("Загрузка из сохранения...")
                
                pet.x = loaded_pet.x
                pet.z = loaded_pet.z
                pet.hp = loaded_pet.hp
                pet.eat = loaded_pet.eat
                pet.stamina = loaded_pet.stamina
                pet.age = loaded_pet.age
                pet.alive = loaded_pet.alive
                pet._Chachka__size = loaded_pet._Chachka__size 
                
                input("\nЗагрузка завершена! Нажмите Enter для продолжения...")
                return pet
            else:
                print("Прервано")
                input("\nEnter для продолжения...")
                return pet
        print("-----------------------")
        
    if data_corrupted: 
        os.rename(filename, f"{filename}.corrupted")
        input("\nEnter для продолжения...")
        return pet

def save_chachka(pet: chachka.Chachka, **k):
    target_dir = os.path.join(".", "saves")
    
    def _check_dir(filename):
        full_path = os.path.join(target_dir, filename)
        if os.path.isfile(full_path) and filename.endswith(".chachka_simulator.save"):
            return filename
        return None
        
    files = list(filter(None, map(_check_dir, os.listdir(target_dir))))
    files.append("Новый файл")

    keys = [*files[:-1], "new"] 
    option, index = pick(files, title="--- Выберите файл сохранения (выбранный файл будет перезаписан!)", indicator="->")
    key = keys[index]

    if key == "new":
        newfile = True
        shutfix = ".chachka_simulator.save"
        filename = f"{input('выберите имя файла сохранения (без расширения): ')}{shutfix}"
        final_save_path = os.path.join(target_dir, filename)
    else:
        newfile = False
        final_save_path = os.path.join(target_dir, key)
    if not newfile:
        if input("вы уверены? [y/N]: ").lower().strip() not in ["y", "н", "д"]:
            rich.print("[#FFFF00][ОТМЕНА][/] Сохранение отменено.")
            return

        if input("вы ТОЧНО УВЕРЕНЫ? [y/N]: ").lower().strip() not in ["y", "н", "д"]:
            rich.print("[#FFFF00][ОТМЕНА][/] Сохранение отменено в последний момент.")
            return
    saves.save(final_save_path, pet)

def command_info(pet: chachka.Chachka, gameclass: ClassGame, **k):
    logs.info("Пользователь Ввел команду информации об чачке", log_path)
    print("==== ИНФОРМАЦИЯ ОБ ЧАЧКЕ ====")
    status = "здоровая" if pet.hp >= 80 else "несильно повреждена" if pet.hp >= 60 else "повреждена" if pet.hp >= 20 else "критически повреждена" if pet.hp >= 5 else "почти умерла"
    print(f"Хп: {pet.hp}, Статус: {status}")
    print(f"Голод: {pet.eat}")
    print(f"Жива: {'Да' if pet.alive else 'Нет'}")
    print(f"Выносливость: {pet.stamina}")
    print(f"прошло тиков времени: {gameclass.ticks_passed}")
    print(f"Координаты чачки: X: {pet.x}, Z: {pet.z}")
    print("=============================")
    input("\nНажмите Enter, чтобы вернуться в меню...")

def command_eat(pet: chachka.Chachka, **k):
    logs.info("Пользователь Ввел команду поедания", log_path)
    print('чачка ест...')
    pet.eating()
    input("\nНажмите Enter, чтобы вернуться в меню...")

def command_step(pet: chachka.Chachka, **k):
    logs.info("Пользователь Ввел команду передвижения", log_path)
    x: Any = input("введите насколько передвинуться чачке по X: ")
    z: Any = input("введите насколько передвинуться чачке по Z: ")
    try:
        x, z = int(x), int(z)
    except (ValueError, TypeError):
        print('некоректные координаты')
        return
    pet.step(x, z)
    input("\nНажмите Enter, чтобы вернуться в меню...")

def command_cheat(pet: chachka.Chachka, map_: maps.Map, conf_path: str, **k):
    logs.info("Пользователь открывает читы...", log_path)
    if CHEATS:
        print("===========================")
        cheat.run(Chack=pet, map_=map_, logging_file_path=log_path, config_path=conf_path)
        print("===========================")
        input("\nНажмите Enter, чтобы вернуться в меню...")
    else:
        rich.print('[#FF0000] ERROR: Доступ запрещен - читы не включены')
        logs.access_denied('Пользователь попытался войти в вкладку читов но запустил игру без этой возможности', log_path)
        input("\nНажмите Enter, чтобы вернуться в меню...")

def command_drawmap(map_: maps.Map, **k):
    logs.info("Пользователь Ввел команду отрисовки карты (drawmap)", log_path)
    draw_map.draw(map_)
    input("\nНажмите Enter, чтобы вернуться в меню...")

def command_use_potions(pet: chachka.Chachka, **k):
    logs.info("Пользователь Ввел команду поглощения зелей", log_path)
    pet.use_potions()
    input("\nНажмите Enter, чтобы вернуться в меню...")

def null(**k):
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
    "save": save_chachka,
    "load": load_chachka,
    "": null
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

    logs.info(f"Игра запущена, Выбран режим игры: {generate_type_txt}", log_path)

    if CHEATS: 
        rich.print('[#FFBB00][WARNING][/] Читы включены')
        logs.warning("Читы включены", log_path)

    pet = chachka.Chachka(age=0.5, x=0, z=0)
    map_game = maps.Map(x1=-5, x2=5, z1=-5, z2=5)
    map_game.link_chack(chachka=pet)

    if generate_type == "-1":
        gen_map.hardgen(map_game)
    elif generate_type == "0":
        gen_map.basegen(map_game)
    elif generate_type == "1":
        gen_map.eazygen(map_game)

    gameclass = ClassGame()
    gameclass.add_map(map_game)

    cheat_config = os.path.abspath(os.path.join("Config", "Cheats.json"))
    while True:
        print("\033[H\033[J", end="")
        menu_title = f"=== Симулятор Чачки ===\nХп: {round(pet.hp, 1)} | Сытость: {round(pet.eat, 1)} | Выносливость: {pet.stamina}\nКоординаты: X: {pet.x}, Z: {pet.z}\nВыберите действие:"
        
        options = [
            'Пропустить',
            'Информация об чачке',
            'Графическая карта',
            'Поесть',
            'Сделать шаг',
            'Выпить зелья вокруг',
            'Крик',
            'сохранить в сохранение',
            'загрузить из сохранения'
        ]
        
        cmd_keys = ['', 'info', 'drawmap', 'eat', 'step', 'use_potions', 'viy', 'save', 'load']
        
        if CHEATS:
            options.append('Открыть чит-меню (Cheat)')
            cmd_keys.append('cheat')

        options.append('Выйти из игры (Exit)')
        cmd_keys.append('exit')
        
        _, index = pick(options, menu_title, indicator='=>')
        
        cmd_key = cmd_keys[index]
        
        if cmd_key == 'exit':
            logs.info('Игра завершена пользователем', log_path)
            break
        if cmd_key == 'load':
            pet = load_chachka(pet, map_game)
            map_game.link_chack(pet)
        elif cmd_key == 'viy':
            menu_title = "=== Выберите тип ==="
            logs.info('пользователь выполнил команду ора чачки (viy / scream)', log_path)
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
                pet.viy(scream)
            elif option == "scream":
                scream = input("насколько громко заорать чачке? (от 8 до 15): ")
                try:
                    scream = max(8, min(15, int(scream)))
                except (ValueError, TypeError):
                    print("неверное значение")
                    continue
                pet.scream(scream)

            input("\nНажмите Enter, чтобы вернуться в меню...")
        else:
            COMMANDS[cmd_key](pet=pet, Gameclass=gameclass, Map=map_game, conf_path=cheat_config)
                
        gameclass.tick()


if __name__ == "__main__":
    run()