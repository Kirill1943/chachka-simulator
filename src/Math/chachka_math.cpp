#include <pybind11/pybind11.h>
#include <cmath>
#include <algorithm>

namespace py = pybind11;

double calculate_stamina(int x, int z) {
    return (std::abs(x) + std::abs(z)) / 100.0 * 40.0;
}

double calculate_removed_hp(double chachka_stamina, double removed_stamina) {
    double overuse = removed_stamina - chachka_stamina;
    
    double actual_overuse = std::max(0.0, overuse); 
    
    return (actual_overuse / 100.0) * 150.0;
}

PYBIND11_MODULE(chachka_math, m) {
    m.doc() = "Математические расчеты на С++ для Симулятора чачки";

    m.def("calculate_stamina", &calculate_stamina, "Расчет траты стамины при шаге чачки",
        py::arg("x"), py::arg("z"));
        
    m.def("calculate_removed_hp", &calculate_removed_hp, "Расчет урона при нулевой стамине",
        py::arg("chachka_stamina"), py::arg("removed_stamina"));
}
