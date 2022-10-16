#! /usr/local/bin/python3

import pandas as pd
from services.da.repos import *

class MartsRepo(object):

    @classmethod
    def get_servers(cls):
        df = pd.DataFrame(repo_servers)
        return df

    @classmethod
    def get_archive(cls):
        df = pd.DataFrame(repo_atchive)
        return df

    @classmethod
    def get_data(cls):
        df = pd.DataFrame(repo_data)
        return df

