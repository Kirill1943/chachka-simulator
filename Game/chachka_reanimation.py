from time import time, sleep
import random

def reanim(chachka):
    if chachka.__class__.__name__ != "Chachka":
        return
    if chachka.alive:
        print("чачка посмотрела на тебя с недоумением, и спросила: Вии! вии ви вии? (эй! слушай зачем мне сердечный массаж сейчас?)")
        return

    print("Реанимация! Тыкай ровно в ритм (2 секунды)!")
    sleep(5)
    chance_dead = 90
    
    print("НАЧИНАЙ!")
    input()
    
    for i in range(1, 6):
        a = time()
        input() 
        b = time()
        
        res = abs(round(b - a, 3))
        error = abs(2.0 - res)
        
        if error <= 0.3:
            chance_dead -= 15
            print(f"Такт {i}: Отличный ритм! Шанс смерти снижен до {chance_dead}%")
        else:
            chance_dead += 5
            print(f"Такт {i}: Ритм сбит... Шанс смерти вырос до {chance_dead}%")


    print("Должна выжить.. Ты надеешься?")
    if input().lower().strip() == "да":
        print("чачка тебя услышала.. она постарается")
        chance_dead -= chance_dead / 100 * 15     
    sleep(2)

    chance_dead = max(2, min(chance_dead, 95))
    
    roll = random.randint(1, 100)
    if roll > chance_dead:
        chachka.hp = 40
        chachka.stamina = 100
        print(f"🎉 ВЫЖИЛА! (Кубик: {roll} при шансе смерти {chance_dead}%)")
    else:
        print("☁️ облачков чачке... ты хочешь ее вернуть?")
        if input().lower().strip() in ["да", "хочу"]:
            print("я тебя услышал... сохранение настроек чачки")
            # TODO: сделать сохранение настроек чачки
        else:
            print("нет?.. поверь - ты мог, но ты не захотел")
