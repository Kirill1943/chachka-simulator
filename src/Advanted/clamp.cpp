#include <pybind11/pybind11.h>
#include <algorithm>

namespace py = pybind11;

int clamp_int(int min, int var, int max) {
    return std::clamp(var, min, max);
}

double clamp_double(double min, double var, double max) {
    return std::clamp(var, min, max);
}

PYBIND11_MODULE(clamp, m) {
    m.doc() = "Ограничение значений на С++ для Симулятора чачки";

    m.def("clamp_int", &clamp_int, "Ограничение целых чисел",
        py::arg("min"), py::arg("var"), py::arg("max"));
        
    m.def("clamp_double", &clamp_double, "Ограничение дробных чисел",
        py::arg("min"), py::arg("var"), py::arg("max"));
}