#include <pybind11/pybind11.h>
#include <string>
#include "opencl_tag.hpp"

// pybind11 module
namespace py = pybind11;

PYBIND11_MODULE(cl_tag, m) {
    py::class_<OPENCL_TAG>(m, "OPENCL_TAG")
        .def(py::init<>())
        .def("tag", &OPENCL_TAG::tag)
        .def("tag_duration", &OPENCL_TAG::tag_duration);
}


