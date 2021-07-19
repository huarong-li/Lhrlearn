import os
import sys

import types
import inspect
from inspect import isfunction

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

from functools import wraps

def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated

@decorator_name
def func():
    return("Function is running")

can_run = True

def func_test():
    global can_run
    print(func())
    # Output: Function is running

    can_run = False
    print(func())
    # Output: Function will not run

def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logit
def addition_func(x):
   """Do some math."""
   return x + x

if __name__ == "__main__":
    func_test()

    addition_func(6)