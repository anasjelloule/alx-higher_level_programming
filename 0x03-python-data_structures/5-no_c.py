#!/usr/bin/python3
def no_c(my_string):
    nw_str = ''
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            nw_str += ch
    return nw_str
