from Game import chachka
from Game.Map import maps, gen_map

def run():
    print('=== Chachka Simulator - симулятор чачки ===')
    print('--- подготовка игры.... ---')
    pet = chachka.Chachka(age=0.5, x=0, z=0)
    map_game = maps.Map(x1=-5, x2=5, z1=-5, z2=5)
    map_game.link_chack(chachka=pet)
    gen_map.basegen(map_game)
    print('--- подготовка окончена ---')
    while True:
        print('введите действие (Exit - выход)')
        cmd = input().strip().lower()
        if cmd == "exit":
            break
        else:
            print('такой команды нету')

if __name__ == "__main__":
    run()