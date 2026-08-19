from dataclasses import dataclass


@dataclass
class HelpStruct:
    name: str
    ru_name: str
    color: str
    description: str
    stats: list[str]