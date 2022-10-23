#! /usr/local/bin/python3

def listToStr(lst):
   
    processing_list = lst
    if processing_list is None or sum( 1 for i in processing_list) == 0: 
        return
    
    converted_list = ' '.join([str(elem) for i, elem in enumerate(processing_list)])
    cmd = mkExeCmd(converted_list)
    return cmd

def mkExeCmd(cmd):
    import re

    if cmd is None and len(cmd) == 0:
        return
    
    # retrieve filename
    fn1 = (re.search(('-name(.*?)-newermt'), cmd)).group(1)
    fn2 = f"{ re.sub('[(){}<>,; ]', '', str(fn1).strip()) }"
    
    # retrieve start date
    ds1 = (re.search(('-newermt(.*?)!'), cmd)).group(1)
    ds2 = f"{ re.sub('[(){}<>,;]', '', str(ds1).strip()) }"
    
    # retrieve end date
    de1 = (re.search(('-newermt.*-newermt(.*?)-ls'), cmd)).group(1)
    de2 = f"{ re.sub('[(){}<>,;]', '', str(de1).strip()) }"
    
    # final replacement
    exe_cmd = str(cmd).replace(fn1, f" '{fn2}' ").replace(ds1, f" '{ds2}' ").replace(de1, f" '{de2}' ")    
    return exe_cmd
             
    
    
    
    