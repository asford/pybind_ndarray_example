# pybind_ndarray_example

Minimial example project demonstrating ndarray/pybind11 support. TLDR? `python setup.py test`.

## Outline

Required dependencies (`ndarray`, `pybind11`, and `Eigen`) are vendorized under
`extern`. `cpp_base.cc` contains a minimal pybind11 module declaring two
structs, support for these structs in pybind11, and a minimal function over
arrays-of-structs. `tests/test_cpp_base.py` demonstrates basic usage of these
functions.

Default ndarray pybind11 support does not support array-of-struct
interconversion with pybind11. A custom type converter, utilizing pybind11's
built-in array and dtype support, is provided under `ndarray_pybind11_converter.hh`.
