import sys

from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

if sys.platform == "win32":
    compile_args = ["/O2", "/std:c++17"]
else:
    compile_args = ["-O3", "-std=c++17", "-march=native"] 

ext_modules = [
    Pybind11Extension(
        "Game.Utils.cpp_math.chachka_math",
        ["src/Math/chachka_math.cpp"],
        include_dirs=["src/Math"],
        extra_compile_args=compile_args
    ),
    Pybind11Extension(
        "Game.Utils.cpp_utils.clamp",
        ["src/Advanted/clamp.cpp"],
        include_dirs=["src/Advanted"],
        extra_compile_args=compile_args
    )
]

setup(
    name="chachka-simulator",
    version="0.2.0",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    package_dir={"": "."}, 
    zip_safe=False,
)
