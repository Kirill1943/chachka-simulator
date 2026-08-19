from pick import pick
from rich import print as rprint

from . import structs as helpstruct
from .data import eat, potions


def check_eat_info(object: helpstruct.HelpStruct):
    ru_name = object.ru_name
    en_name = object.name

    stats = '\n'.join(object.stats)
    description = object.description
    color = object.color

    rprint("------------------------")
    rprint(f"Имя: [{color}]{ru_name} ({en_name})")
    rprint(f"Описание: {description}")
    rprint(f"--- Статы ---\n{stats}")
    rprint("------------------------")

    input("вернуться к документации...")

def check_potion_info(object: helpstruct.HelpPotionStruct):

    en_effect_name = object.effect_name
    ru_effect_name = object.ru_effect_name

    en_potion_name = object.potion_name
    ru_potion_name = object.ru_potion_name

    stats = {lvl: "\n".join(items) for lvl, items in object.levels.items()}

    description = object.description
    color = object.color

    rprint("------------------------")
    rprint(f"Имя зелья: [{color}]{ru_potion_name}[/] ([italic]{en_potion_name}[/])")
    rprint(f"Имя эффекта: [{color}]{ru_effect_name}[/] ([italic]{en_effect_name}[/])")
    rprint(f"Описание: {description}")
    rprint("------------- Статы -------------")
    
    for lvl, lvl_stats in stats.items():
        rprint(f"Уровень {lvl}")
        rprint(f"    {lvl_stats}")
        
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
                        options = [i.ru_potion_name for i in potions.ITEMS]
                        option, index = pick(options, menu_title, indicator="=>")

                        check_potion_info(potions.ITEMS[index])
            case "exit":
                return