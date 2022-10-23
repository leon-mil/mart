#! /usr/local/bin/python3

from functools import wraps
import datetime as dt
import inspect

# def timer_decorator(arg, opt=None):
#     def timer_decorator_outter(fn):
#         @wraps(fn)
#         def timer_decorator_inner(*args, **kwargs):
            
#             # start timer
#             start = dt.datetime.now()
            
#             # execute function
#             response = fn(*args, **kwargs)
            
#             # end timer
#             end = dt.datetime.now()
            
#             # calculate time difference
#             delta_cal = end - start
            
#             print('Function executed in sec::msec: {}:{}'.format(delta_cal.seconds, delta_cal.microseconds))
            
#             return response
#         return timer_decorator_inner
#     return timer_decorator_outter

def timer_decorator(func): 
    @wraps(func)
    def wrapper(*args, **kwargs):
        
        # start timer
        start = dt.datetime.now()
        
        # execute function
        response = func(*args, **kwargs)
        
        # end timer
        end = dt.datetime.now()
        
        # calculate time difference
        delta_cal = end - start
        
        print('\nFunction \'{}\' executed in [sec]:[msec]: [{}]:[{}]'.format(wrapper.__name__, delta_cal.seconds, delta_cal.microseconds))
        
        return response
    return wrapper
