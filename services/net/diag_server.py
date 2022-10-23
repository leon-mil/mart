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

def ping5(servers):
    
    # The command you want to execute   
    cmd = 'ping'
  
    # send one packet of data to the host 
    # this is specified by '-c 1' in the argument list 
    outputlist = []
    # Iterate over all the servers in the list and ping each server
    for server in servers:
        temp = subprocess.Popen([cmd, '-c 1', server], stdout = subprocess.PIPE) 
        # get the output as a string
        output = str(temp.communicate()) 
        # store the output in the list
        outputlist.append(output)
    return outputlist
      
  