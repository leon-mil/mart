#! /usr/local/bin/python3

from services.net.diag_flogs import *
from services.utils.dates.date_util import *
from services.utils.run_subprocess import *
from types import * 
import datetime as dt

"""
      Programer: Leon Mil
           Date: 10/17/2022
    Description: Returns True if log exits based on date range.
        Execute: find test type -f -name 'file*' -newermt '2022-10-11 10:00:00' ! -newermt '2022-10-11 13:00:00' '-ls'
""" 
def check_logs(**kargs):
      
    hours_in_past = 2
    hours_in_future = 1
    delta_min = 5
    
    # start from now
    date_in_start = dt.datetime.now().replace(microsecond=0)
    
    # create a date range by subtracting hours from the start date
    date_in_past = date_in_start - dt.timedelta(hours=hours_in_past)
    
    # create a date range by subtracting hours from the start date
    date_in_future = date_in_start + dt.timedelta(hours=hours_in_future)
    
    # create time delta obj used to subtract time by the min intervals. The size of each step in min.
    date_in_delta = dt.timedelta(minutes=1, microseconds=0)
    
    date_in_end   = (date_in_start + (5 * date_in_delta)).replace(microsecond=0)
    
    # print('  Date Range Start: {}'.rjust(20).format(date_in_start))
    # print('   Date Range Past: {}'.rjust(20).format(date_in_past))
    # print(' Date Range Future: {}'.rjust(20).format(date_in_future))
    # print('    Date Range End: {}'.rjust(20).format(date_in_end))
    # print('  Date Range Delta: {}'.rjust(20).format(date_in_delta))

    file_dir    = 'test'
    file_name   = 'file*'
    date_start  = f'{ date_in_start }'
    date_end    = f'{ date_in_end   }'
    
    final_return = list()
    
    options = {
        'f1' : False,
        'f2' : False,
        'f3' : False,
        'f4' : True
    }
    options.update(kargs)

    if options.get('f1'):
        ###############################################
        # Run via fileExists function with 4 args
        ###############################################
        f1 = fileExists(file_dir, file_name, date_start, date_end)
        print('Run method [fileExists for f1] result: {}'.format(f1))
    
    if  options.get('f2'):   
        ###############################################
        # Run via fileExists function with 2 args
        ###############################################
        f2 = fileExists(file_dir, file_name)
        print('Run method [fileExists for f2] result: {}'.format(f2))
        
    if options.get('f3'):
        ###############################################
        # Run via run 2nd overload function 
        ###############################################
        cmd = ['find', file_dir, '-name', file_name, '-newermt', date_start, '!', '-newermt', date_end, '-ls']
        out = 'logs/files_out.log'
        err = 'logs/files_err.log'
    
        f3 = run(cmd, out, err, stdout=True, stderr=False)
        print('\nFunction \'{}\' returned: {}'.format(run.__name__, f3))
        #print("\nThe wrapped functions docstring is:", run.__doc__)
        
    if options.get('f4'):
        ###############################################
        # imports
        ###############################################
        # from services.utils.dates.date_util import daterange
        # from services.utils.dates.date_util import create_date
        
        ###############################################
        # Run via run 2nd overload function 
        ###############################################
        #cmd = ['find', file_dir, '-name', file_name, '-newermt', date_start, '!', '-newermt', date_end, '-ls']
        out = 'logs/files_out.log'
        err = 'logs/files_err.log'
        
        ##############################################
        # Dates
        ##############################################
       
        
        ##############################################
        # Loop through time delta
        ##############################################
        
       
        
        # How many minutes
        # total_min = 4
        # start_date = datetime.datetime.now()
        # min_delta_size = datetime.timedelta(minutes=2)
        # end_date   = start_date + (total_min * min_delta_size)
        
        # date_range = int(((end_date - start_date).seconds) / 60)
        # print('Minutes: {}'.format(date_range))
        
        # for min in range(date_range):
        #     date = start_date + timedelta(minutes=float(min))
        #     print(date.replace(microsecond=0))
            
        
        # s = '2022-10-26 01:01:00:00'
        # e = '2022-10-26 01:06:00:00'
        # start = convert_to_datetime(s)
        # end   = convert_to_datetime(e)
        
        # start = datetime.datetime.now().replace(microsecond=0)
        # end   = (start + (4 * datetime.timedelta(minutes=1))).replace(microsecond=0)
        
        # interval = DateFormat.MIN
        # step = 1
        
        # for i in daterange(start, end, step, interval):
        #     print(i)
        
                
        # for date_current in range( (date_in_end - date_in_start).min):
        #     print('  Date Range Start: {}'.rjust(20).format(date_in_start))
        #     print('     Iterator Date: {}'.rjust(20).format(date_current))
        #     print('    Date Range End: {}'.rjust(20).format(date_in_end))
            
            
        # print('  Date Range Start: {}'.rjust(20).format(date_in_start))
        # print('   Date Range Past: {}'.rjust(20).format(date_in_past))
        # print(' Date Range Future: {}'.rjust(20).format(date_in_future))
        # print('    Date Range End: {}'.rjust(20).format(date_in_end))
        # print('  Date Range Delta: {}'.rjust(20).format(date_in_delta))
        # print('     Iterator Date: {}'.rjust(20).format(date_current))
        
        # cmd = ['find', file_dir, '-name', file_name, '-newermt', f'{ date_current }', '!', '-newermt', date_end, '-ls']
        
        # f4 = run(cmd, out, err, stdout=True, stderr=False) 
        # print('\nFunction \'{}\' returned: {}'.format(run.__name__, f4))
        #print("\nThe wrapped functions docstring is:", run.__doc__)
        
        """_summary_
        file_dir    : search directory
        file_name   : name of the file
        out         = STDOUT is redirected to the specified log file. Format: 'logs/files_out.log'
        err         = STDERR is redirected to the specified log file. Format: 'logs/files_err.log'
        step        = Total number of hours from the current date and time 
        step_size   = Specifies with element to pick while indexing. So a step size of 1 is every element, a step size of 2 means alternate elements, and so on. 
        """
        funcargs = { 'file_dir' : file_dir, 'file_name' : file_name, 'out' : out, 'err' : err, 'step' : 2, 'step_zize' : 1 }
        res = find(run, funcargs)
        
        process_return, process_output = res[0], res[1]
        print('Did the process execute successfully: {}'.rjust(50).format(process_return))
        print('Did the process returned data: {}'.rjust(50).format(process_output))
   
        if options.get('f1'): final_return.append(f1)
        if options.get('f2'): final_return.append(f2)
        if options.get('f3'): final_return.append(f3)
        #if options.get('f4'): final_return.append(f4)
        
    return final_return

    
    
    
    
  