import json
import os
from datetime import datetime

import Chachka
import rich


def save(load_file, pet: Chachka.Chachka):
    date = datetime.now()
    
    save_data = {
        "time": {
            "hh:mm:ss": f"{date.hour:02d}:{date.minute:02d}:{date.second:02d}",
            "date": f"{date.day:02d}.{date.month:02d}.{date.year}"
        },
        "coords": {
            "x": getattr(pet, "x", 0),
            "y": getattr(pet, "y", 0)
        },
        "size": getattr(pet, "size", [30, 30, 30]),
        "pet": {
            "alive": {
                "is_alive": pet.alive,
                "hp": pet.hp
            },
            "stamina": pet.stamina,
            "eat": pet.eat,
            "age": pet.age
        }
    }

    try:
        with open(load_file, "w", encoding="utf-8") as file:
            json.dump(save_data, file, ensure_ascii=False, indent=4)
        rich.print(f'[#00FF00][SUCCESS][/] Игра успешно сохранена в {load_file}')
    except Exception as e:
        rich.print(f'[#FF0000][ERROR][/] Не удалось записать файл сохранения: {e}')
        return False
        
    return True


def load(load_file, link_map=None): # TODO: переписать эту функцию загрузки
    chachka_object = Chachka.Chachka(age=0, x=0, y=0)
    
    if not os.path.exists(load_file):
        rich.print(f'[#FF0000][ERROR][/] Файл сохранения {load_file} не найден!')
        return None
        
    with open(load_file, "r", encoding="utf-8") as file:
        try:
            settings = json.load(file)
        except json.JSONDecodeError as e:
            rich.print(f'[#FF0000][ERROR][/] Ошибка декодирования сохранения: {e}')
            return None 
        
        coords = settings.get("coords", {})
        chachka_object.x = coords.get("x", 0)
        chachka_object.y = coords.get("y", 0)
        

        pet_data = settings.get("pet", {})
        alive_data = pet_data.get("alive", {})
        
        chachka_object.alive = alive_data.get("is_alive", True)
        chachka_object.hp = alive_data.get("hp", 100)
        chachka_object.stamina = pet_data.get("stamina", 100)
        chachka_object.eat = pet_data.get("eat", 100)
        chachka_object.age = pet_data.get("age", 0)
        
        allowed_sizes = [[6, 6, 6], [30, 30, 30], [80, 80, 80]]
        size_data = settings.get("size", [30, 30, 30])
        
        if size_data == ["?", "?", "?"] or size_data not in allowed_sizes:
            size_data = [30, 30, 30]
            
        chachka_object.set_size(size_data)
        chachka_object.in_map = link_map
        
        rich.print(f'[#00FF00][SUCCESS][/] Сохранение успешно загружено!')
        return chachka_object
