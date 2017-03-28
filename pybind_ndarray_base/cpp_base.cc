#include "stdint.h"
#include <iostream>

#include "pybind11/pybind11.h"
#include "pybind11/numpy.h"
#include "numpy/arrayobject.h"

#include "ndarray.h"
#include "ndarray_pybind11_converter.hh"

struct ExampleStruct {
  double a;
  int b;
};

struct NestedExampleStruct {
  ExampleStruct ex1;
  ExampleStruct ex2;
  bool flag;
};

void sum_example_struct(ndarray::Array<ExampleStruct, 1> input, ndarray::Array<double, 1> out) {
  if(input.getSize<0>() != out.getSize<0>()) {
    throw std::invalid_argument("Invalid array shapes");
  }

  for(std::size_t i = 0; i < input.getSize<0>(); ++i) {
    out[i] = input[i].a + input[i].b;
  }
}

void sum_example(
    ndarray::Array<double, 1> a,
    ndarray::Array<double, 1> b,
    ndarray::Array<double, 1> out
) {
  if((a.getSize<0>() != b.getSize<0>()) || (a.getSize<0>() != out.getSize<0>())) {
    throw std::invalid_argument("Invalid array shapes");
  }

  for(std::size_t i = 0; i < a.getSize<0>(); ++i) {
    out[i] = a[i] + b[i];
  }
}

PYBIND11_PLUGIN(cpp_base){
  // _import_array initializes numpy api, needed for ndarray/array interconversion
  std::cout << "init" << std::endl;

  if (_import_array() < 0) {
    PyErr_SetString(
        PyExc_ImportError, "numpy.core.multiarray failed to import");
    return nullptr;
  };

  pybind11::module m("cpp_base", "Pybind ndarray cpp-level example.");
  namespace py = pybind11;

  PYBIND11_NUMPY_DTYPE(ExampleStruct, a, b);

  std::cout << "def_sum_example" << std::endl;
  m.def("sum_example", &sum_example);

  std::cout << "def_example_struct" << std::endl;
  m.def("sum_example_struct", &sum_example_struct);

  std::cout << "def_real_dtype" << std::endl;
  m.attr("real_dtype") = py::dtype::of<double>();

  std::cout << "def_struct_dtype" << std::endl;
  m.attr("struct_dtype") = py::dtype::of<ExampleStruct>();

  return m.ptr();
}
