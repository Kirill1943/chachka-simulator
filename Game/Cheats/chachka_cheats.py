import json
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Game import logging as logs
from Game.Chachka import Chachka
from Game.game import ClassGame


def set_ticks(ticks: int, game_class: ClassGame):
    try:
        ticks = int(ticks)
    except (ValueError, TypeError):
        return
    game_class.ticks_passed = ticks

def set_chachka_hp(hp: int, chachka: Chachka):
    try:
        hp = int(hp)
    except (ValueError, TypeError):
        return
    chachka.hp = max(0, min(hp, 100))

def set_chachka_stamina(stamina: int, chachka: Chachka):
    try:
        stamina = int(stamina)
    except (ValueError, TypeError):
        return
    chachka.stamina = max(0, min(stamina, 100))

def set_chachka_eat(eat: int, chachka: Chachka):
    try:
        eat = int(eat)
    except (ValueError, TypeError):
        return
    chachka.eat = max(0, min(eat, 100))

def set_chachka_immortality(immortality: bool, config_path: str, log_path: str):
    if os.path.exists(config_path) and os.path.isfile(config_path):
        with open(config_path, "r", encoding="utf-8") as conf:
            try:
                jsonconf = dict(json.load(conf))
                jsonconf["immortality"] = immortality
            except json.JSONDecodeError:
                logs.warning(f"Файл конфигурации читов битый / пустой / не формата JSON, перезапись конфига на стандартный...", file_path=log_path)
                jsonconf = {
                    "immortality": immortality
                }
        
        with open(config_path, "w", encoding="utf-8") as conf:
            json.dump(jsonconf, conf, indent=4, ensure_ascii=False)
            
    else:
        logs.error(f"Попытка открыть файл который должен был являться конфигурацией игры провалилась\nпричина ошибки: файла несуществует\nфайл который попытались открыть: {config_path}", file_path=log_path)
        return