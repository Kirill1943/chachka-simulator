import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import structs as helpclasses

INSTANT_REGENERATION_POTION = helpclasses.HelpPotionStruct(
    effect_name="instant regeneration",
    ru_effect_name="моментальная регенерация",
    potion_name="instant regeneration potion",
    ru_potion_name="зелье моментальной регенерации",
    color="#D20000",
    description="водянное безвкусное зелье регенерации, довольно красное. без вкуса но спасает от смерти",
    levels={
        1: ["+8 к здоровью"],
        2: ["+14 к здоровью"],
        3: ["+29 к здоровью"],
        4: ["+41 к здоровью"],
        5: ["+65 к здоровью"]
    }
)

ITEMS = [
    INSTANT_REGENERATION_POTION
]