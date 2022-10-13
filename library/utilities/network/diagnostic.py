#! /usr/local/bin/python3

import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import os

"""
      Programer: Leon Mil
           Date: 10/9/2022
    Description: Returns True if host (str) responds to a ping request.
                 Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
"""
def ping(host):
    
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0

def ping2(host):
    icmp_num = 1 #ICMP Echo Number
    os.system('ping -q -c {} {}'.format(icmp_num, host))

def ping3(host):
    
     # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'
    
    try:
        response = subprocess.check_output(
            ['ping', '-c', '1', host],
            stderr=subprocess.STDOUT,  # get all output
            universal_newlines=True  # return string not bytes
        )
    except subprocess.CalledProcessError:
        response = None

def ping4(host) -> is_up:
    with open(os.devnull, 'w') as DEVNULL:
        try:
            result = subprocess.check_call(
                ['ping', '-c', '1', host],
                stdout=DEVNULL,  # suppress output
                stderr=DEVNULL
            )
            is_up = True
            #return (result == 0)
        except subprocess.CalledProcessError:
            is_up = False