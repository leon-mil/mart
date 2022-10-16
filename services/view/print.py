#! /usr/local/bin/python3

from lib.deff.view.decor import *

def print1(*args, title):
    
    #  put a generator on all elements in args that will
    #  use string.format to prepend / append custom wrapper or text to all args
    
    # First iteration wraps passed argument in a header and footer.
    # args = [ '{} {} {}'.format(header, index, footer) for index in args ]
    args = [ '{} {}'.format(header, index) for index in args ]
    
    for index, value in enumerate(args):
        args[index] = value.replace( "{title}", (title + ' ' + str(index + 1)) )
    
    # pass it on to print()
    print(*args)
    
def print2(**kwargs):
    #kwargs = { '{} {}'.format(header, key) for key in kwargs }
    
    right_aligned_dict = { host.rjust(13): state.rjust(14) for host, state in kwargs.items()}
    
    # for key,value in kwargs.items():
    #     print("{0:20}{1:5d}".format(key,value))

    for host, state in right_aligned_dict.items():
        print(host + ": " + state)
    
    # for host in kwargs:
    #     print('{0:10} {1:30}'.format(host, kwargs[host]))
        
    print('\n')