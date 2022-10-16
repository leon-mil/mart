#! /usr/local/bin/python3

import pandas as pd

repo_servers = {
    'server':   ['steps21', 'steps23',  'steps28'],
    'state':    ['Active',  'Active',   'Active']
}

repo_atchive = {
    'server':   ['steps23'],
    'statp':    ['202209'],
    'archive':  ['a202209'],
    'logname1': ['Active'],
    'logname2': ['Active'],
    'date':     ['2022-10-11 10:00:00']
}

repo_data = {
    'server':   ['steps21', 'steps23',  'steps28'],
    'statp':    ['202209',  '202209',   '202209'],
    'data':     ['d202209', 'd202209',  'd202209']
}