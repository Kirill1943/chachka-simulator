import json
import os

import Chachka

DEFAULT_SETTINGS_FILE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "saves", "save_1.json"))

def load(load_file=DEFAULT_SETTINGS_FILE, link_map=None):
    chachka_object = Chachka.Chachka(age=0, x=0, y=0)
    
    if os.path.exists(load_file):
        with open(load_file, "r", encoding="utf-8") as file:
            try:
                settings = dict(json.load(file))
            except json.JSONDecodeError as e:
                print(f'[ERROR] ошибка декодирования сохранения: {e}')
                return None 
            else:
                coords = settings.get("Coords", {})
                chachka_object.x = coords.get("x", 0)
                chachka_object.z = coords.get("z", 0)
                
                allowed_sizes = [[6, 6, 6], [30, 30, 30], [80, 80, 80]]
                size_data = settings.get("Size", [30, 30, 30])
                
                if size_data == ["?", "?", "?"] or size_data not in allowed_sizes:
                    size_data = [30, 30, 30]
                chachka_object.set_size(size_data)
                chachka_object.in_map = link_map
                
                return chachka_object
    return None