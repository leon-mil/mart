#! /usr/local/bin/python3
from datetime import timedelta
import datetime
import functools
from tracemalloc import stop
from lib.enums.date_format import DateFormat

def create_date(datetime_str, datetime_format='%d/%m/%Y %H:%M:%S.%f'):
    from datetime import datetime as dt
    
    dt_format = '%d/%m/%Y %H:%M:%S.%f'
    
    # Given timestamp in string '24/7/2021 11:13:08.230010'
    dt_str = datetime_str

    # create datetime object from timestamp string
    dt_result = dt.strptime(dt_str, dt_format).replace(microsecond=0)
    
    return dt_result

'''
Date Formats: 
fmt = '%Y-%m-%d'
fmt = '%m/%d/%Y %H:%M:%S'
fmt = "%Y-%m-%d %H:%M:%S"
fmt = "%Y-%m-%dT%H:%M:%S"
'''
def convert_to_datetime(date_str:str='2022-12-30 00:00:01'):

    # Import the datetime class
    from datetime import datetime

    # Write a format string to parse s
    date_format = '%Y-%m-%d %H:%M:%S:%f'

    # Create a datetime object date_converted
    date_converted = datetime.strptime(date_str, date_format)
    
    return date_converted

def seconds_to_dhms(time):
    seconds_to_minute   = 60
    seconds_to_hour     = 60 * seconds_to_minute
    seconds_to_day      = 24 * seconds_to_hour

    days    =   time // seconds_to_day
    time    %=  seconds_to_day

    hours   =   time // seconds_to_hour
    time    %=  seconds_to_hour

    minutes =   time // seconds_to_minute
    time    %=  seconds_to_minute

    seconds = time

    print("%d days, %d hours, %d minutes, %d seconds" % (days, hours, minutes, seconds))

def daterange(start, end, step=1, interval=DateFormat.DAY):
    from lib.enums.date_format import DateFormat
    from datetime import datetime as dt
    
    def count_timedelta(delta:timedelta, step:int, intervals_sec:int):
        """Helper function for iterate.  Finds the number of intervals in the timedelta."""
        return int(delta.total_seconds() / (intervals_sec * step) + 1)
    
    intervals = functools.partial(count_timedelta, (end - start), step)
    
    match interval:
        case DateFormat.WEEK:
            for i in range(intervals(3600 * 24 * 7)):
                yield start + datetime.timedelta(weeks=i) * step
        case DateFormat.DAY:
            for i in range(intervals(3600 * 24)):
                yield start + datetime.timedelta(days=i) * step
        case DateFormat.HOUR:
            for i in range(intervals(3600)):
                yield start + datetime.timedelta(hours=i) * step
        case DateFormat.MIN:
            for i in range(intervals(60)):
                yield start + datetime.timedelta(minutes=i) * step
        case DateFormat.SEC:
            for i in range(intervals(1)):
                yield start + datetime.timedelta(seconds=i) * step
        case DateFormat.MILLISECOND:
            for i in range(intervals(1 / 1000)):
                yield start + datetime.timedelta(microseconds=i) * step
        case DateFormat.MICROSECOND:
            for i in range(intervals(1e-6)):
                yield start + datetime.timedelta(microseconds=i) * step
        case _:
            raise AttributeError("Interval must be 'week', 'day', 'hour' 'second', \
                'microsecond' or 'millisecond'.")

"""
      Programer: Leon Mil
           Date: 10/26/2022
    Description: Returns True if a file exits based on date range.
                 Function check for file in the past.
        Execute: find test type -f -name 'file*' -newermt '2022-10-11 10:00:00' ! -newermt '2022-10-11 13:00:00' '-ls'
""" 
def find(func, funcargs):
    """_summary_
    Descripton:
        Function used to find a specific file in the past starting from the current date and time.
    Arguments:
        file_dir    : search directory
        file_name   : name of the file
        out         = STDOUT is redirected to the specified log file. Format: 'logs/files_out.log'
        err         = STDERR is redirected to the specified log file. Format: 'logs/files_err.log'
        step        = Total number of hours from the current date and time 
        step_size   = Specifies with element to pick while indexing. So a step size of 1 is every element, a step size of 2 means alternate elements, and so on. 
    Returns:
        tuple: process_output - True if command produced output
               process_return - True if command successfully ran
    """
    options = {
        'file_dir'  : 'test',
        'file_name' : 'file*',
        'out'       : 'logs/files_out.log',
        'err'       : 'logs/files_err.log',
        'step'      : 2,
        'step_size' : 1,
    }
    options.update(funcargs)
    
    file_dir    = options.get('file_dir')
    file_name   = options.get('file_name')
    out         = options.get('out')
    err         = options.get('err')
    step        = options.get('step')
    step_size   = options.get('step_size')
    
    # start checking from the specified time in the past
    step_hours = int(step)
    
    # stop checking when we reach current time
    stop_date = datetime.datetime.now().replace(microsecond=0)
    
    # step interval
    delta_size = datetime.timedelta(hours=int(step_size), microseconds=0, milliseconds=0)
    
    # start checking from the specified time in the past
    start_date  = (stop_date - (step_hours * delta_size)).replace(microsecond=0)

    cmd = ['find', file_dir, '-name', file_name, '-newermt', f'{ start_date }', '!', '-newermt', f'{ stop_date }', '-ls']
    res = func(cmd, out, err, stdout=True, stderr=False) 
  
    return res
    
    

