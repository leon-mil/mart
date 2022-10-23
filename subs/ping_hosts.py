#! /usr/local/bin/python3

#region imports
# Ping functionality
from services.net.diag_server import *

# Decorator functions
from lib.deff.view.decor import *

# Domain definitions
from lib.deff.net.domain import *

# Importing print functions used for printing ping results
from services.view.print import *
#endregion

# Hosts defined in the Domain defitions import
hosts = [steps21, steps23, steps28]


def get_ping_results():
    # Clear host log
    with open('logs/hosts.log', 'w'): pass

    results = {}
    for host in hosts: 
        results[host] = 'Destination Host Reachable' if ping4(host) else 'Destination Host Unreachable' 
        
    # Defined in the services.view.print 
    return results


def print_ping_results():
    
    # See wrapper avove 
    result = get_ping_results()
    
    # call print.py from services.view.print.py
    print2(**result)