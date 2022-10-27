#! /usr/local/bin/python3

import os
from services.da.get import *
from services.da.repos import *
from services.utils.decorators.timer import *

if __name__ == '__main__': 
    
    ##############################################
    # Control
    ##############################################
    flag_ping_hosts = False
    flag_get_ripo   = False
    flag_get_logs   = True

    ###############################################
    # Ping Hosts
    ###############################################
    if flag_ping_hosts: 
        import subs.ping_hosts as ph
        ph.print_ping_results()

    ###############################################
    # Get Ripo
    ###############################################
    if flag_get_ripo:
        import subs.get_repos as gr
        gr.get_repos()

    ###############################################
    # Logs
    ###############################################
    if flag_get_logs:
        import subs.check_logs as cl
        result = cl.check_logs(f1=False, f2=False, f3=False, f4=True)
        print('File: \'main\' commulitave return of f1, f2 and f3 is: {} \n'.format(result))