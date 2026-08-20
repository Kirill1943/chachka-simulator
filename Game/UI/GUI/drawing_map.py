import os.path
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import tkinter as tk

from Game.Chachka import Chachka
from Game.Gameplay.items import Eat_items as eat
from Game.Gameplay.items import Potion_items as potion
from Game.Gameplay.Map.maps import Map


def draw(map_instance: Map):
    width = map_instance.x2 - map_instance.x1 + 1
    height = map_instance.z2 - map_instance.z1 + 1

    window_size = 440
    cell_width = window_size // width
    cell_height = window_size // height

    try:
        root = tk.Tk()
        root.title("Карта Игры (GUI)")
        
        canvas = tk.Canvas(
            root, 
            width=window_size, 
            height=window_size, 
            bg="white"
        )
        canvas.pack(padx=10, pady=10)

        for r in range(height):
            for c in range(width):
                x1 = c * cell_width
                y1 = r * cell_height
                x2 = x1 + cell_width
                y2 = y1 + cell_height
                
                canvas.create_rectangle(
                    x1, y1, x2, y2, 
                    fill="#E0E0E0", 
                    outline="#A0A0A0"
                )

        for item in map_instance.objects:
            cell_x = item.x - map_instance.x1
            cell_z = item.z - map_instance.z1
            
            if 0 <= cell_x < width and 0 <= cell_z < height:
                x1 = cell_x * cell_width
                y1 = cell_z * cell_height
                x2 = x1 + cell_width
                y2 = y1 + cell_height
                
                
                if isinstance(item, eat.Apple):
                    canvas.create_rectangle(
                        x1, y1, x2, y2, 
                        fill="#00AA00", 
                        outline="#A0A0A0"
                    )
                elif isinstance(item, eat.Apple_slice):
                    offset_x = cell_width // 4
                    offset_y = cell_height // 4
                    canvas.create_rectangle(
                        x1 + offset_x, y1 + offset_y, 
                        x2 - offset_x, y2 - offset_y, 
                        fill="#88FF00", 
                        outline="#A0A0A0"
                    )
                elif isinstance(item, potion.instant_regenerate_potion):
                    if 1 <= item.effect.level <= 5:
                        color = "#9B0000" if 1 <= item.effect.level <= 3 else "#FF0000"
                        canvas.create_rectangle(
                            x1, y1, x2, y2,
                            fill=color, 
                            outline="#A0A0A0"
                        )
        for chack in map_instance.chaks:
            cell_x = chack.x - map_instance.x1
            cell_z = chack.z - map_instance.z1
            
            if 0 <= cell_x < width and 0 <= cell_z < height:
                x1 = cell_x * cell_width
                y1 = cell_z * cell_height
                x2 = x1 + cell_width
                y2 = y1 + cell_height
                
                if isinstance(chack, Chachka):
                    canvas.create_rectangle(
                        x1, y1, x2, y2, 
                        fill="#8B5A2B", 
                        outline="#A0A0A0"
                    )

        lbl_chack = tk.Label(root, text="■ Коричневый — Чачка", fg="#8B5A2B", font=("Arial", 10, "bold"))
        lbl_chack.pack(anchor="w", padx=15)

        lbl_apple = tk.Label(root, text="■ Зелёный — Целое яблоко (на всю клетку)", fg="#00AA00", font=("Arial", 10, "bold"))
        lbl_apple.pack(anchor="w", padx=15)

        lbl_slice = tk.Label(root, text="■ Салатовый — Кусочек яблока (частично)", fg="#88FF00", font=("Arial", 10, "bold"))
        lbl_slice.pack(anchor="w", padx=15)

        lbl_regeneration_potion_levels13 = tk.Label(root, text="■ темно-красный - зелье регенерации 1-3 уровня (на всю клетку)", fg="#9B0000", font=("Arial", 10, "bold"))
        lbl_regeneration_potion_levels13.pack(anchor="w", padx=15)

        lbl_regeneration_potion_levels45 = tk.Label(root, text="■ темно-красный - зелье регенерации 4-5 уровня (на всю клетку)", fg="#FF0000", font=("Arial", 10, "bold"))
        lbl_regeneration_potion_levels45.pack(anchor="w", padx=15)

        btn_close = tk.Button(root, text="Вернуться в игру", command=root.destroy)
        btn_close.pack(pady=10)

        root.mainloop()

    except (tk.TclError, KeyboardInterrupt):
        print("--- Окно карты закрыто. Возврат в консоль ---")