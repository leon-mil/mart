#! /usr/local/bin/python3

from asyncore import dispatcher_with_send
from urllib import response
from services.net.diag_flogs import *
from services.utils.run_subprocess import *
from multipledispatch import dispatch
from types import * 



"""
      Programer: Leon Mil
           Date: 10/17/2022
    Description: Returns True if log exits based on date range.
        Execute: find test type -f -name 'file*' -newermt '2022-10-11 10:00:00' ! -newermt '2022-10-11 13:00:00' '-ls'
""" 
def check_logs(**kargs):
    
    file_dir    = 'test/'
    file_name   = 'file*'
    date_start  = '2022-10-11 10:00:00'
    date_end    = '2022-10-11 13:00:00'
    
    final_return = list()
    
    options = {
        'f1' : False,
        'f2' : False,
        'f3' : False
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
        
    if options.get('f1'): final_return.append(f1)
    if options.get('f2'): final_return.append(f2)
    if options.get('f3'): final_return.append(f3)
        
    return final_return
