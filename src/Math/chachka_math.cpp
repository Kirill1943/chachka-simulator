#include <pybind11/pybind11.h>
#include <cmath>

namespace py = pybind11;
using namespace std;

double calculate_stamina(int x, int z) {
    double stamina = (std::abs(x) + std::abs(z)) / 100.0 * 40.0;
    return stamina;
}

double calculate_removed_hp(double chachka_stamina, double removed_stamina) {
    double overuse = removed_stamina - chachka_stamina;
    double removed_xp = overuse / 100.0 * 150.0;

    return removed_xp;
}

PYBIND11_MODULE(chachka_math, m) {
    m.doc() = "Математические расчеты на С++";

    m.def("calculate_stamina", &calculate_stamina, "Расчет траты стамины при шаге чачки");
    m.def("calculate_removed_hp", &calculate_removed_hp, "Расчет урона при нулевой стамине");
}
