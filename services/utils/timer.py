#! /usr/local/bin/python3

from functools import wraps

def timer_decorator(arg, opt=None):
    def timer_decorator_outter(fn):
        @wraps(fn)
        def timer_decorator_inner(*args, **kwargs):
            response = fn(*args, **kwargs)
            return response
        return timer_decorator_inner
    return timer_decorator_outter