#! /usr/local/bin/python3

from services.da.get import *
from services.da.repos import *

###############################################
# Get Ripos
###############################################
def get_repos():
    df_data = MartsRepo.get_data()
    print(df_data)

    print('\n')

    df_arch = MartsRepo.get_archive()
    print(df_arch)

    print('\n')

    df_serv = MartsRepo.get_servers()
    print(df_serv)

    print('\n')