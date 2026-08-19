from dataclasses import dataclass


@dataclass
class HelpStruct:
    name: str
    ru_name: str
    color: str
    description: str
    stats: list[str]

@dataclass
class HelpPotionStruct:
    effect_name: str
    ru_effect_name: str
    potion_name: str
    ru_potion_name: str
    color: str
    description: str
    levels: dict[int, list[str]]