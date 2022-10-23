#! /usr/local/bin/python3

#region imports
from datetime import datetime
import subprocess
from multipledispatch import dispatch
from types import *                     # We can test for lambda type, e.g.:
#endregion

#region Function Overload: fileExists
"""
      Programer: Leon Mil
           Date: 10/17/2022
    Description: Returns True if log exits based on date range.
       Commands:
                  # cmd1 = ['find ' + dir + ' -type f' + "-name " + file + ' -newermt ' + '"' + begin + '"' + ' ! ' + '-newermt ' + '"' + end + '"', ' -ls']
                  # cmd2 = "find " + dir + " -type f " + "-name " + file + " -newermt " + "\'" + begin + "\'" + " ! " + "-newermt " + "\'" + end + "\'" + " -ls"
                  # cmd3 = "find " + dir + " -type f " + "-name " + file + " -newermt " + begin + " ! " + "-newermt " + end + " -ls"
                  # cmd4 = ['find', fdir, '-type', 'f', '-name', fnam, '-newermt', dbgn, '!', '-newermt', dend, '-ls']
"""
@dispatch((str, tuple, list), 
          (str, tuple, list))
def fileExists(dir, file):
    
    if (dir or file) is None:
        return False
    
    with open('logs/files.log', 'a') as file_log: 
        
        command = "find " + dir + " -type f " + "-name " + file + " -ls"
        
        try:
            child = subprocess.Popen (
                command,         
                stdout=file_log,
                stderr=file_log,
                shell=True
            )
            result = child.wait() == 0
        except subprocess.CalledProcessError as e:
            result = False
            file_log.write('Method: fileExists -> Standard Error: ' + str(e.stderr) + '\n')
            file_log.write('Method: fileExists -> Standard Outpu: ' + str(e.stdout) + '\n')

        return result
#endregion

#region Function Overload: fileExists
"""
      Programer: Leon Mil
           Date: 10/17/2022
    Description: Returns True if log exits based on date range.
       Commands:
                  # cmd1 = ['find ' + dir + ' -type f' + "-name " + file + ' -newermt ' + '"' + begin + '"' + ' ! ' + '-newermt ' + '"' + end + '"', ' -ls']
                  # cmd2 = "find " + dir + " -type f " + "-name " + file + " -newermt " + "\'" + begin + "\'" + " ! " + "-newermt " + "\'" + end + "\'" + " -ls"
                  # cmd3 = "find " + dir + " -type f " + "-name " + file + " -newermt " + begin + " ! " + "-newermt " + end + " -ls"
                  # cmd4 = ['find', fdir, '-type', 'f', '-name', fnam, '-newermt', dbgn, '!', '-newermt', dend, '-ls']
"""
@dispatch((str, tuple, list), 
          (str, tuple, list), 
          (str, tuple, list, datetime, object), 
          (str, tuple, list, datetime, object))
def fileExists(dir, file, begin, end):
    
    if (dir or file or begin or end) is None:
        return False
    
    with open('logs/files.log', 'a') as file_log: 
        
        command = "find " + dir + " -type f " + "-name " + file + " -newermt " + "\'" + begin + "\'" + " ! " + "-newermt " + "\'" + end + "\'" + " -ls"
        
        try:
            child = subprocess.Popen (
                command,         
                stdout=file_log,
                stderr=file_log,
                shell=True
            )
            result = child.wait() == 0
        except subprocess.CalledProcessError as e:
            result = False
            file_log.write('Method: fileExists -> Standard Error: ' + str(e.stderr) + '\n')
            file_log.write('Method: fileExists -> Standard Outpu: ' + str(e.stdout) + '\n')

        return result
#endregion





    



    