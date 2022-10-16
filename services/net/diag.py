#! /usr/local/bin/python3

from asyncio.subprocess import DEVNULL, PIPE
from logging import captureWarnings
import platform
from stat import filemode    # For getting the operating system name
import subprocess  # For executing a shell command
import os
from sys import stderr
from unittest import result
from urllib import response

"""
      Programer: Leon Mil
           Date: 10/9/2022
    Description: Returns True if host (str) responds to a ping request.
                 Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
"""
def ping(host):
    
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'
    
    #ICMP Echo Number
    icmp_num = '1' 

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, icmp_num, host]
    
    with open('logs/hosts.log', 'a') as file_log:
        result = subprocess.call(
            command,
            stdout=file_log,
            stderr=file_log,
            text=True)
    
    return ( result == 0 )

def ping2(host):
    
     # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'
    
    #ICMP Echo Number
    icmp_num = '1' 
    
    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, icmp_num, host]
    
    try:
        response = subprocess.check_output(
            command,
            stderr = subprocess.STDOUT, # get all output
            universal_newlines = True   # return string not bytes
        )
    
    except subprocess.CalledProcessError:
        response = None
        
    return response

def ping3(host):
    
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'
    
    #ICMP Echo Number
    icmp_num = '1' 
    
    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, icmp_num, host]
    
    with open(os.devnull, 'w') as DEVNULL:
        try:
            result = subprocess.check_call(
                command,
                stdout=DEVNULL,  # suppress output
                stderr=DEVNULL
            )
            is_up = (result == 0)
        except subprocess.CalledProcessError as e:
            is_up = (e.returncode == 0)
        
        return is_up
    
def ping4(host):
    
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    #ICMP Echo Number
    icmp_num = '1' 

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, icmp_num, host]
    
    try:
        with open('logs/hosts.log', 'a') as file_log: 
            
            child = subprocess.run(
                command,
                stdout=file_log,
                stderr=file_log)
            
            result = (child.returncode == 0)
            
    except subprocess.SubprocessError as e:
        result = False
        
    return result
      
        
def fileExists(filename):
    
    with open('logs/files.log', 'a') as file_log: 
        
        command = ['ls', '-ltr', filename]
        
        try:
            result = subprocess.run (
                command, 
                capture_output=False,   # If capture_output is true, stdout and stderr will be captured.
                text=True,              # If text mode is not used, stdin, stdout and stderr will be opened as binary streams. We will need to use.decode().
                check=True,             # If returncode is non-zero, raise a CalledProcessError.
                stdout=file_log,
                stderr=file_log
            )
            file_exists = (result.returncode == 0)
        except subprocess.CalledProcessError as e:
            file_exists = False
            file_log.write('STD ERR: ' + str(e.stderr) + '\n')
            file_log.write('STD OUT: ' + str(e.stdout) + '\n')

        return (file_exists)

def fileExistsDateRange(filename, dtstart, dtend):
    
    #region hide
    # with open('logs/files.log', 'a') as file_log: 
        
    #     date_start = "2022-10-11 09:00:00"
    #     date_end = "2022-10-11 10:00:00"
        
    #     #find -newermt "2017-11-06 17:30:00" ! -newermt "2017-11-06 22:00:00" -ls
        
    #     command = ['find', '-newermt', date_start, '!', '-newermt', date_end, '-ls']
        
    #     try:
    #         result = subprocess.run (
    #             command, 
    #             capture_output=False,   # If capture_output is true, stdout and stderr will be captured.
    #             text=True,              # If text mode is not used, stdin, stdout and stderr will be opened as binary streams. We will need to use.decode().
    #             check=True,             # If returncode is non-zero, raise a CalledProcessError.
    #             stdout=file_log,
    #             stderr=file_log
    #         )
    #         file_exists = (result.returncode == 0)
    #     except subprocess.CalledProcessError as e:
    #         file_exists = False
    #         file_log.write('STD ERR: ' + str(e.stderr) + '\n')
    #         file_log.write('STD OUT: ' + str(e.stdout) + '\n')

    #     return (file_exists)
    #endregion
    
    # date_start = "2022-10-11 09:00:00"
    # date_end = "2022-10-11 10:00:00"
        
    date_start = dtstart
    date_end = dtend
    
    #find ./file* -newermt "2012-10-11 09:00:00" ! -newermt "2022-10-11 11:00:00" -ls
    
    cmd1 = ['find ' + filename + ' -type f' + ' -newermt ' + '"' + date_start + '"' + ' ! ' + '-newermt ' + '"' + date_end + '"', ' -ls']
    cmd2 = "find " + filename + " -type f -newermt " + "\'" + date_start + "\'" + " ! " + "-newermt " + "\'" + date_end + "\'" + " -ls"
    cmd3 = "find " + filename + " -type f -newermt " + date_start + " ! " + "-newermt " + date_end + " -ls"
    
    
    # proc = subprocess.Popen(['/usr/bin/find', '/path/to/dir', '-type', 'f',
    #                      '-name', '*.gradle', '-exec', 'grep', 'KEYWORD',
    #                      '{}', '/dev/null', ';'],
    #                      stdout=PIPE, stderr=PIPE)

    # result = subprocess.run(cmd2, shell=True)
    
    result = subprocess.Popen(cmd1, shell=True)
    
    file_exists = (result.returncode == 0)
    return (file_exists)
    