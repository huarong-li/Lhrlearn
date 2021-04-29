#!/usr/bin/env python

"""
setup.py file for SWIG example
"""

import sys

from distutils.core import setup, Extension

example_module = Extension('_example',
                           sources=['invoke/example_wrap.cxx', 'example.cpp'],
                           )

setup (name = 'example',
       version = '1.0.1',
       author      = "SWIG Docs",
       description = """Simple swig example from docs""",
       packages=['foxit'],
       ext_package='foxit',
       ext_modules = [example_module],
       py_modules = ["foxit/example"],
       )
