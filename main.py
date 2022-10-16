#! /usr/local/bin/python3

import os
from services.da.get import *
from services.da.repos import *
from services.utils.timer import *


# fn = 'file*'
# dir = '~/dev/work/marts/test/'
# ds = "'2022-10-11 10:00:00'"
# dn = "'2022-10-11 13:00:00'"

# filename = '~/dev/work/marts/test/file*'
# date_start = '2022-10-11 10:00:00'
# date_end = '2022-10-11 13:00:00'

#  p1 = fileExistsDateRange(filename, ds, dn)

# print('STDERR: \n' + 'No Errors \n' if (len(p1.stderr)==0) else p1.stderr + '\n' )
# print('STDOUT: \n' + p1.stdout)
       
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

###############################################
# Ping Hosts
###############################################
import subs.ping_hosts as ph
ph.print_ping_results()

###############################################
# Get Ripo
###############################################
import subs.get_repos as gr
gr.get_repos()
