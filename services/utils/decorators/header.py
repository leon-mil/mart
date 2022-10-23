#! /usr/local/bin/python3

def header_decorator(arg, opt=None):
    from functools import wraps
    import lib.deff.view.decor as hf
    from services.utils.conversions.custom.list_to_str import listToStr
    def header_decorator_outter(fn):
        @wraps(fn)
        def header_decorator_inner(*args, **kwargs):
            
            # custom header
            print('{}'.format(hf.header_long_notitle))
            print('* Function: {}'.format( header_decorator_inner.__name__) )
            print('*  Command: {}'.format( listToStr(args[0]) ) if len(args) > 0 and args[0] is not None else '')
            print('{}'.format(hf.footer_long_notitle))
            
            # execute function
            response = fn(*args, **kwargs)
            
            # custom footer
            print('{}'.format(hf.footer_long_notitle))
             
            return response
        return header_decorator_inner
    return header_decorator_outter
