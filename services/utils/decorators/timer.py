#! /usr/local/bin/python3

from functools import wraps
import datetime as dt
import inspect

# region commented out
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
#endregion

def timer_decorator(func):
    import time
    @wraps(func)
    def wrapper(*args, **kwargs):
        
        # Total time in sec since the Epoch.
        start_time_epoch = time.time()
        
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
          
        # Wall time end: 
        elapsed_time_wall = dt.datetime.now() - start_time_wall
        
        # Epoch elapsed timeL
        elapsed_time_epoch = time.time() - start_time_epoch
        elapsed_time_epoch_msec = round(elapsed_time_epoch * 1000)
        
        fn = wrapper.__name__
        epoch_hms = time.strftime("%H:%M:%S", time.gmtime(elapsed_time_epoch))
        epoch_ms = time.strftime("%M:%S", time.gmtime(elapsed_time_epoch))
        epoch_s = time.strftime("%S", time.gmtime(elapsed_time_epoch))
        
        print('\n  CPU execution time of function \'{}\' in [S]:[M]: [{}:{}]'.format(fn, round(elapsed_time_cpu), round((elapsed_time_cpu * 1000))))
        print(' Wall execution time of function \'{}\' in [S]:[M]: [{}:{}]'.format(fn, round(elapsed_time_wall.seconds), round(elapsed_time_wall.microseconds)))
        print('Epoch execution time of function \'{}\' in [S]:[M]: [{}:{}]'.format(fn, epoch_s, elapsed_time_epoch_msec))
        return response
    return wrapper
