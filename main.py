#! /usr/local/bin/python3

from library.utilities.network.diagnostic import *
from library.utilities.display.print import *
from library.definitions.network.domain import *


hosts = [steps21, steps23, steps28]

results = {}
for host in hosts: 
    results[host] = 'Destination Host Reachable' if ping4(host) else 'Destination Host Unreachable' 
        
#print1(*hosts, title = "Host")
print2(**results)

