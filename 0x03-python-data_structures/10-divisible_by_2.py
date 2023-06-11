#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nw_lst = [elm % 2 == 0 for elm in my_list]
    return nw_lst
