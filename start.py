import os
import sys

from Game import Chachka
from Game.Cheats import main_cheat as cheat
from Game.game import ClassGame
from Game.Map import gen_map, maps
from Game.UI import drawing_map_GUI as draw_map

Dir_File = os.path.dirname(os.path.abspath(__file__))
Full_Cheats_Path = os.path.abspath(os.path.join(Dir_File, "Config", "Cheats.json"))

if "--cheats" in sys.argv:
    CHEATS = True
else:
    CHEATS = False

def run():
    print('=== Chachka Simulator - симулятор чачки ===')
    print('[WARNING] Читы включены')
    print('--- подготовка игры.... ---')
    pet = Chachka.Chachka(age=0.5, x=0, z=0)
    map_game = maps.Map(x1=-5, x2=5, z1=-5, z2=5)
    map_game.link_chack(chachka=pet)
    gen_map.basegen(map_game)
    Gameclass = ClassGame()
    Gameclass.add_map(map_game)
    print('--- подготовка окончена ---')
    
    while True:
        print('введите действие (Exit - выход, Info - информация об чачке, dwawmap: отрисовать карту)')
        if CHEATS: print('(Читы активированы, Введите Cheat для открытия читов)')
        cmd = input().strip().lower()
        
        if cmd == "exit":
            break
        elif cmd == "info":
            print(f"==== ИНФОРМАЦИЯ ОБ ЧАЧКЕ ====")
            status = "здоровая" if pet.hp >= 80 else "несильно повреждена" if pet.hp >= 60 else "повреждена" if pet.hp >= 20 else "критически повреждена" if pet.hp >= 5 else "почти умерла"
            print(f"Хп: {pet.hp}, Статус: {status}")
            print(f"Голод: {pet.eat}")
            print(f"Жива: {'Да' if pet.alive else 'Нет'}")
            print(f"Выносливость: {pet.stamina}")
            print(f"прошло тиков времени: {Gameclass.ticks_passed}")
            print(f"=============================")
        elif cmd == "drawmap":
            draw_map.draw(map_game)
        elif cmd == "cheat" and CHEATS:
            print("===========================")
            cheat.run()
            print("===========================")
        else:
            print('такой команды нету')
            
        Gameclass.tick()


if __name__ == "__main__":
    run()