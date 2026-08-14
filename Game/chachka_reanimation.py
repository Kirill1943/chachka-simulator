import json
import os
import secrets
import sys
from time import sleep, time

import rich
from pick import pick

from Game.Utils.cpp_utils.clamp import clamp_int as clamp


def reanim(chachka):
    if chachka.__class__.__name__ != "Chachka":
        return
        
    if chachka.hp <= 0:
        chachka.alive = False

    if chachka.alive and chachka.hp > 0:
        rich.print("[#00FF00]Чачка посмотрела на тебя с недоумением, и спросила: Вии! вии ви вии? (эй! слушай зачем мне сердечный массаж сейчас?)[/]")
        return

    history_text = "🚨 РЕАНИМАЦИЯ! Тыкай Enter ровно в ритм (каждые 2 секунды)! 🚨\n\n"

    rich.print("\n[#FF0000]🚨 РЕАНИМАЦИЯ! Тыкай Enter ровно в ритм (каждые 2 секунды)! 🚨[/]")
    rich.print("[#AAAAAA]Приготовься... Игра начнется через 5 секунд.[/]")
    sleep(5)
    chance_dead = 90
    
    rich.print("\n[#00FF00]🔥 НАЧИНАЙ! (Нажми Enter для первого такта) 🔥[/]")
    input()
    
    for i in range(1, 6):
        a = time()
        input(f"Такт {i}/5 [Жми Enter!] ") 
        b = time()
        
        res = abs(round(b - a, 3))
        error = abs(2.0 - res)
        
        if error <= 0.3:
            chance_dead -= 15
            line = f"Такт {i}: Отличный ритм! ({res} сек). Шанс смерти снижен до {clamp(2, chance_dead, 95)}%"
            rich.print(f"[#00FF00]{line}[/]")
        else:
            chance_dead += 5
            line = f"Такт {i}: Ритм сбит... ({res} сек). Шанс смерти вырос до {clamp(2, chance_dead, 95)}%"
            rich.print(f"[#FF5555]{line}[/]")
            
        history_text += line + "\n"

    menu_title = f"{history_text}\nДолжна выжить.. Ты надеешься?\nВы верите?"
    hope_options = ["Да, я верю в Чачку!", "Нет, уже всё равно..."]
    _, hope_index = pick(hope_options, menu_title, indicator="=>")
    
    if hope_index == 0:
        history_text += "\nЧачка тебя услышала.. она постарается!\n"
        chance_dead -= (chance_dead / 100 * 15)     
    else:
        history_text += "\nТы не веришь в Чачку...\n"
        
    rich.print("[#00FF00]Считаем шансы...[/]")
    sleep(2)

    chance_dead = clamp(2, chance_dead, 95)
    roll = secrets.randbelow(100) + 1
    
    if roll > chance_dead:
        chachka.hp = 40
        chachka.eat = 40
        chachka.stamina = 100
        chachka.alive = True
        print("\033[H\033[J", end="")
        rich.print(f"🎉 [bold #00FF00]ВЫЖИЛА![/] (Кубик: {roll} при шансе смерти {round(chance_dead, 1)}%)")
        input("\nНажмите Enter, чтобы продолжить игру...")
    else:
        death_title = f"☁️ Облачков чачке... (Кубик: {roll} при шансе смерти {round(chance_dead, 1)}%)\nТы хочешь ее вернуть?"
        revive_options = ["Да, вернуть её!", "Нет, пусть покоится с миром", "Нет, мне плевать как-то"]
        _, revive_index = pick(revive_options, death_title, indicator="=>")
        
        if revive_index == 0:
            pth = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Config", "Chachka.json"))
            
            if os.path.exists(pth):
                with open(pth, "r", encoding="utf-8") as file:
                    Settings = dict(json.load(file))
                if Settings.get("Save_Chachka", False):
                    rich.print("[#00FF00]Я тебя услышал... восстановление в сохранение...[/]")
                    # TODO: реализовать сохранение настроек
                    input("\nНажмите Enter для продолжения...")
                    return
            
            rich.print('[#FF0000]Я бы мог, но ты не настроил конфиг на бессмертность чачки... Game Over[/]')
            sys.exit()
        else:
            rich.print("[#AAAAAA]Нет?.. Поверь — ты мог попробовать, но ты не захотел.[/]")
            sys.exit()
