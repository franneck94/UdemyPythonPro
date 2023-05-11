#include <pybind11/pybind11.h>

namespace py = pybind11;

void clip_vector(py::list in, double min_value, double max_value) {
    size_t idx = 0;
    auto it_in = in.begin();

    for (; it_in != in.end(); ++it_in, ++idx)
    {
        const double curr_val = it_in->cast<double>();

        if (curr_val < min_value)
        {
            in[idx] = min_value;
        }
        else if (curr_val > max_value)
        {
            in[idx] = max_value;
        }
    }
}

PYBIND11_MODULE(math_cpp_python, m) {
    m.def("clip_vector", &clip_vector, "doc...");
}
