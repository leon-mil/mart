#! /usr/local/bin/python3

from multiprocessing.connection import wait
from subprocess import *
from xmlrpc.client import DateTime
from multipledispatch import dispatch
from types import *
from services.utils.decorators.timer import *

"""
      Programer: Leon Mil
           Date: 10/17/2022
    Description: Returns True if log exits based on date range.
"""
@timer_decorator
def run(command, logout, logerr, stdout=False, stderr=False):
    """Execute a linux command and write results to the log.

    Args:
        name: command | type:           (list): A command to be executed with the run function.
        name: logout  | type:            (str): The path to the subprocess.popen STDOUT log script.
        name: logerr  | type:            (str): The path to the subprocsss.popen STDERR log script. 
        name: stdout  | type: (bool, optional): If set to True, the STDOUT will output to the screen. Defaults to False.
        name: stderr  | type: (bool, optional): If set to True, the STDERR will output to the screen. Defaults to False.

    Raises:
        error: CalledProcessError
        error: RuntimeError

    Returns:
        bool: True if subprocess.peopen return code was 0 and False otherwise.
    """
    import datetime as dt
    from io import StringIO
    
    with open(logout, "at") as file_out_log, \
         open(logerr, "at") as file_err_log:
        try:
            popen = Popen(
                        command, 
                        stdout=PIPE, 
                        stderr=PIPE,
                        universal_newlines = True)
            
            # stdout 
            file_out_log.write(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            for line in popen.stdout: 
                file_out_log.write(line)
                print(line, end = '') if stdout else StringIO().write(line)
             
             # stderr 
            file_err_log.write(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")  
            for line in popen.stderr: 
                file_err_log.write(line)
                print(line, end = '') if stderr else StringIO().write(line)
            
            return_code = popen.wait()
            result = (return_code == 0)
                   
            error_message = ('The process call "{}" returned with code {}. '
                             'The return code is not 0, thus an error occurred.'
                             .format(list(command), return_code))
            
        except CalledProcessError as error: 
            result = error.returncode == 0
            raise error(error_message)
        except RuntimeError as error: 
            result = False
            raise error(error_message)
    
    return result