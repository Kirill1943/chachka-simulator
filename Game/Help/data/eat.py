import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import structs as helpclasses

APPLE = helpclasses.HelpStruct(
    name="Apple",
    ru_name="Яблоко",
    color="#7BFF00",
    description="обычное съедобное аппетитное яблоко",
    stats=["+ от 25 до 40 единиц сытости"]
)

APPLE_SLICE = helpclasses.HelpStruct(
    name="Apple_slice",
    ru_name="кусочек яблока",
    color="#7BFF00",
    description="недоеденное яблоко, выглядит неаппетитно но иногда единственное что спасает",
    stats=["+ от 4 до 9 единиц сытости"]
)

ITEMS = [
    APPLE,
    APPLE_SLICE
]