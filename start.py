from Game import Chachka
from Game.game import ClassGame
from Game.Map import gen_map, maps
from Game.UI import drawing_map_GUI as draw_map


def run():
    print('=== Chachka Simulator - симулятор чачки ===')
    print('--- подготовка игры.... ---')
    pet = Chachka.Chachka(age=0.5, x=0, z=0)
    map_game = maps.Map(x1=-5, x2=5, z1=-5, z2=5)
    map_game.link_chack(chachka=pet)
    gen_map.basegen(map_game)
    Gameclass = ClassGame()
    Gameclass.add_map(map_game)
    print('--- подготовка окончена ---')
    
    while True:
        print('введите действие (Exit - выход, Info - информация об чачке)')
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
        else:
            print('такой команды нету')
            
        Gameclass.tick()


if __name__ == "__main__":
    run()