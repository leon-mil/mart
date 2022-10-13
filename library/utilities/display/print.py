#! /usr/local/bin/python3

from library.definitions.display.decorator import *
# from termcolor import colored

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
    
    for host in kwargs:
        print('{} {}'.format(host, kwargs[host]))