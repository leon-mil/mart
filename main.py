#! /usr/local/bin/python3

from library.utilities.network.diagnostic import *
from library.utilities.display.print import *
from library.definitions.network.domain import *


hosts = [steps21, steps23, steps28]

# Clear log
with open('logs/hosts.log', 'w'): pass

results = {}
for host in hosts: 
    results[host] = 'Destination Host Reachable' if ping4(host) else 'Destination Host Unreachable' 

filename = 'logs/hosts2.log'
p1 = fileExists(filename)
print('STDERR: \n' + 'No Errors \n' if (len(p1.stderr)==0) else p1.stderr + '\n' )
print('STDOUT: \n' + p1.stdout)
       
#print1(*hosts, title = "Host")
#print2(**results)

