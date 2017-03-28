#!/usr/bin/env python2
from ez_setup import use_setuptools
use_setuptools(version="19")

import os
from os import path
import re

import numpy

from setuptools import setup, find_packages, Extension

import subprocess

pybind_srcs = [
    "pybind_ndarray_base/cpp_base.cc",
]


# See http://stackoverflow.com/questions/29048623/does-setuptools-build-ext-behaves-differently-from-distutils-one
# Setuptools requires dot-separated module name, while distutils may accepts "/" separated paths
pybind_modules = [
    Extension(
        # Convert source file name to module name
        path.splitext(src)[0].replace("/", "."),
        [src],
        include_dirs=[
            path.join(path.dirname(__file__), "pybind_ndarray_base"),
            path.join(path.dirname(__file__), "extern", "include"),
            numpy.get_include(),
        ],
    ) for src in pybind_srcs
]

for m in pybind_modules:
    m.extra_compile_args += ['-std=c++11']

setup(
    name="pybind_ndarray_base",
    description="Example ndarray/pybind11 interaction.",
    author="Alex Ford",
    author_email="fordas@uw.edu",
    url="https://github.com/asford/pybind_ndarray_base/",
    provides=["pybind_ndarray_base"],
    packages=find_packages(),
    ext_modules=pybind_modules,
    install_requires=[
        "numpy>=1.9",
    ],
    test_suite="pybind_ndarray_base.tests",
)
