from pick import pick
from rich import print as rprint

from .check_info import check_eat_info, check_potion_info
from .data import eat, potions

ITEMS = []
ITEMS.extend(eat.ITEMS)
ITEMS.extend(potions.ITEMS)

def run():
    while True:
        print("\033[H\033[J", end="")
        menu_title = "--- Выберите пункт документации: ---"
        options = [
            "Информация об объектах",
            "Обозначения объектов на нарисованной карте (drawmap)",
            "Выйти"
        ]
        keys = ["descript", "color-values", "exit"]
        option, index = pick(options, menu_title, indicator="=>")
        key = keys[index]

        match key:
            case "descript":
                menu_title = "--- выберите тип объектов: ---"
                options = [
                    "Еда",
                    "Зелья"
                ]
                keys = ["eat", "potions"]
                option, index = pick(options, menu_title, indicator="=>")
                key = keys[index]
                match key:
                    case "eat":
                        menu_title = "--- выберите еду информацию которой нужно просмотреть: ---"
                        options = [i.ru_name for i in eat.ITEMS]
                        option, index = pick(options, menu_title, indicator="=>")

                        check_eat_info(eat.ITEMS[index])
                    case "potions":
                        menu_title = "--- выберите зелье информацию о котором нужно просмотреть: ---"
                        options = [i.ru_name for i in potions.ITEMS]
                        option, index = pick(options, menu_title, indicator="=>")

                        check_potion_info(potions.ITEMS[index])
            case "color-values":
                rprint("----------- обозначения обьектов на карте -----------")
                for obj in ITEMS:
                    rprint(f'{obj.ru_name}: [{obj.color}]{obj.color}')
                print("-----------------------------------------------------")
                input("вернуться к документации...")
            case "exit":
                return