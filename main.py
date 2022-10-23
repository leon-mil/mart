#! /usr/local/bin/python3

import os
from services.da.get import *
from services.da.repos import *
from services.utils.decorators.timer import *

       
# d1 = dt.date.today()
# print(d1)
###############################################
#
###############################################
# d2 = dt.datetime.now()
# d2 = d2.replace(microsecond=0)
# print(d2)

# d3 = dt.timedelta(minutes=5)

# d4 = d2 - d3
# print(d4)
###############################################
# Create and subtract dates
###############################################
# d3 = dt.datetime(2022, 10, 11, 10, 0, 0)
# print(d3)

# d4 = d3 - d2
# print(d4)


##############################################
# Loop through time delta
##############################################
# The size of each step in days
# day_delta = dt.timedelta(days=1)

# start_date = dt.date.today()
# end_date = start_date + 7*day_delta

# for i in range((end_date - start_date).days):
#     print(start_date + i*day_delta)


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
    result = cl.check_logs(f1=False, f2=False, f3=True, f4=True)
    print('File: \'main\' commulitave return of f1, f2 and f3 is: {} \n'.format(result))