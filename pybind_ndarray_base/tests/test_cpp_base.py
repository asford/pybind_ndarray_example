from unittest import TestCase

import pybind_ndarray_base.cpp_base as cpp_base

import numpy
import numpy.testing

class TestBase(TestCase):
    def test_basic(self):
        inp = numpy.arange(10, dtype=numpy.float)
        out = numpy.empty(10)

        cpp_base.sum_example(inp, inp, out)
        numpy.testing.assert_almost_equal(inp + inp, out)

    def test_struct(self):
        inp = numpy.empty(10, dtype=cpp_base.struct_dtype)
        inp["a"] = numpy.arange(10)
        inp["b"] = 10

        out = numpy.empty(10)

        cpp_base.sum_example_struct(inp, out)
        numpy.testing.assert_almost_equal(inp["a"] + inp["b"], out)
