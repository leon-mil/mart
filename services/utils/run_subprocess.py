#! /usr/local/bin/python3

from asyncio import subprocess
from concurrent.futures import process
from subprocess import check_output
from services.utils.decorators.header import header_decorator
from services.utils.decorators.timer import timer_decorator

"""
      Programer: Leon Mil
           Date: 10/17/2022
    Description: Returns True if log exits based on date range.
"""
@header_decorator('')
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
    from datetime import datetime 
    from subprocess import Popen, PIPE, STDOUT, CalledProcessError
    from io import StringIO
    
    with open(logout, "at") as file_out_log, \
         open(logerr, "at") as file_err_log:
        try:
            popen = Popen(
                        command, 
                        stdout=PIPE, 
                        stderr=PIPE,
                        universal_newlines = True)
            
            capture_output = None
            capture_return = None
            
            # stdout 
            file_out_log.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            for line in popen.stdout: 
                capture_output = True if (len(str(line)) > 0) else False
                file_out_log.write(line)
                print(line, end = '') if stdout else StringIO().write(line)
             
            # stderr 
            file_err_log.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")  
            for line in popen.stderr: 
                file_err_log.write(line)
                print(line, end = '') if stderr else StringIO().write(line)
                
            return_code = popen.wait()
            capture_return = (return_code == 0)
            
            popen.stdout.flush()
                   
            error_message = ('The process call "{}" returned with code {}. '
                             'The return code is not 0, thus an error occurred.'
                             .format(list(command), return_code))
         
        except FileNotFoundError:
            capture_return = False
            raise error(error_message)
        except KeyboardInterrupt as kb:
            capture_return = False
            exit()   
        except CalledProcessError as error: 
            capture_return = error.returncode == 0
            raise error(error_message)
        except RuntimeError as error: 
            capture_return = False
            raise error(error_message)
    
    return (capture_return, capture_output)