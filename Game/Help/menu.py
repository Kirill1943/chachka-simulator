import structs as helpstruct
from pick import pick
from rich import print as rprint

from .data import eat


def check_eat_info(object: helpstruct.HelpStruct):
    ru_name = object.ru_name
    en_name = object.name
    stats = '* \n'.join(object.stats)
    description = object.description
    color = object.color

    rprint("------------------------")
    rprint(f"Имя: [{color}]{ru_name}")
    rprint(f"Имя в игре: [{color}]{en_name}")
    rprint(f"Описание: {description}")
    rprint(f"Статы:\n{stats}")
    rprint("------------------------")

    input("вернуться к документации...")

def run():
    while True:
        menu_title = "--- Выберите пункт документации: ---"
        options = [
            "Информация об обьектах",
            "Выйти"
        ]
        keys = ["descript", "exit"]
        option, index = pick(options, menu_title, indicator="=>")
        key = keys[index]

        match key:
            case "descript":
                menu_title = "--- выберите тип обьектов: ---"
                options = [
                    "Еда"
                ]
                keys = ["eat"]
                option, index = pick(options, menu_title, indicator="=>")
                key = keys[index]
                match key:
                    case "eat":
                        menu_title = "--- выберите вещь информацию которой нужно просмотреть: ---"
                        options = [i.ru_name for i in eat.ITEMS]
                        option, index = pick(options, menu_title, indicator="=>")

                        check_eat_info(eat.ITEMS[index])
            case "exit":
                return