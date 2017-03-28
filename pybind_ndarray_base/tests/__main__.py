import sys
import pybind_ndarray_base.tests

result = pybind_ndarray_base.tests.test()
sys.exit(not result.wasSuccessful())
