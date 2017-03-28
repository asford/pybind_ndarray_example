import unittest


def test():
    return unittest.TextTestRunner().run(unittest.defaultTestLoader.discover("pybind_ndarray_base.tests"))
