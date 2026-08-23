from rich import print as rprint

from . import structs as helpstruct


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

    en_potion_name = object.name
    ru_potion_name = object.ru_name

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