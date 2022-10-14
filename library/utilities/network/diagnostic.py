#! /usr/local/bin/python3

from asyncio.subprocess import DEVNULL, PIPE
from logging import captureWarnings
import platform
from stat import filemode    # For getting the operating system name
import subprocess  # For executing a shell command
import os
from sys import stderr

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
    
    with open('logs/network/diagnostic.log', 'w') as file_log:
        result = subprocess.call(
            command,
            stdout=file_log,
            stderr=file_log)
    
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
      
    with open('logs/hosts.log', 'a') as file_log: 
        # p1 = subprocess.run(command, capture_output=True, text=True)
        # p2 = subprocess.run(command, stdout=PIPE, text=True)
        p3 = subprocess.run(command, stdout=file_log, text=True)
        #print(p3.stdout)
        
def fileExists(filename):
    
    with open('logs/files.log', 'a') as file_log: 
        command = ['ls', '-ltr', filename]
        
        try:
            result = subprocess.run(
                command, 
                capture_output=True,    # If capture_output is true, stdout and stderr will be captured.
                text=True,              # If text mode is not used, stdin, stdout and stderr will be opened as binary streams. We will need to use.decode().
                check=True,             # If returncode is non-zero, raise a CalledProcessError.
                stdout=file_log
            )
        except subprocess.CalledProcessError as e:
            print(e.stderr)
    
    return (result.returncode == 0)
    
    