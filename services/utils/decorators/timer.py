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

# def timer_decorator(func): 
#     @wraps(func)
#     def wrapper(*args, **kwargs):
        
#         # start timer
#         start = dt.datetime.now()
        
#         # execute function
#         response = func(*args, **kwargs)
        
#         # end timer
#         end = dt.datetime.now()
        
#         # calculate time difference
#         delta_cal = end - start
        
#         print('\nFunction \'{}\' executed in [sec]:[msec]: [{}]:[{}]'.format(wrapper.__name__, delta_cal.seconds, delta_cal.microseconds))
        
#         return response
#     return wrapper

def timer_decorator(func):
    import time
    import timeit
    @wraps(func)
    def wrapper(*args, **kwargs):
        
        # CPU execution start time:
        start_time_cpu = time.process_time()
        
         # Wall start time:
        start_time_wall = dt.datetime.now()
        
        ########################################################
        # Execute main function
        response = func(*args, **kwargs)
        ########################################################
        
        # CPU execution time elapsed in sec
        elapsed_time_cpu = time.process_time() - start_time_cpu
        
        # CPU execution time elapsed in msec
        elapsed_time_msec = elapsed_time_cpu * 1000
        
        # Wall time end: 
        elapsed_time_wall = dt.datetime.now() - start_time_wall
        
        print('\n  CPU execution time of function \'{}\' in [sec]:[msec]: [{}]:[{}]'.format(wrapper.__name__, elapsed_time_cpu, (elapsed_time_cpu * 1000)))
        print(' Wall execution time of function \'{}\' in [sec]:[msec]: [{}]:[{}]'.format(wrapper.__name__, elapsed_time_wall.seconds, elapsed_time_wall.microseconds))
        
        return response
    return wrapper
