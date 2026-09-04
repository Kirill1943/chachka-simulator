import json
import os
from datetime import datetime
from typing import TYPE_CHECKING
from Chachka import Chachka

if TYPE_CHECKING:
    from Gameplay.Map.maps import Map

def save(load_file: str, pet: Chachka) -> bool:
    date = datetime.now()
    
    save_data = {
        "time": {
            "hh:mm:ss": f"{date.hour:02d}:{date.minute:02d}:{date.second:02d}",
            "date": f"{date.day:02d}.{date.month:02d}.{date.year}"
        },
        "coords": {
            "x": getattr(pet, "x", 0),
            "z": getattr(pet, "z", 0)
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
    except Exception:
        return False
        
    return True

def load(load_file: str, link_map: Map | None = None) -> tuple[Chachka, str] | tuple[None, None]:
    chachka_object = Chachka(age=0, x=0, z=0)

    if os.path.isfile(load_file):
        with open(load_file, "r", encoding="utf-8") as f:
            try:
                readed = json.load(f) 
            except json.JSONDecodeError:
                return (None, None)
        
        time_data = readed.get("time", {})
        date = f'{time_data.get("date", "XX.XX.XXXX")} {time_data.get("hh:mm:ss", "??:??:??")}'
        
        coords = readed.get("coords", {})
        x = coords.get("x", 0)
        z = coords.get("z", 0)
        
        size = readed.get("size", [6, 6, 6])
        pet = readed.get("pet", {})
        pet_alive = pet.get("alive", {})

        chachka_object.x, chachka_object.z = x, z
        chachka_object._Chachka__size = size
        chachka_object.alive = pet_alive.get("is_alive", True)
        chachka_object.hp = pet_alive.get("hp", 100)
        chachka_object.eat = pet.get("eat", 100)
        chachka_object.stamina = pet.get("stamina", 100)
        chachka_object.age = pet.get("age", 0)
        chachka_object.in_map = link_map

        return (chachka_object, date)
    else:
        return (None, None)