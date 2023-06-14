#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nw_lst = my_list[:]
    for i in range(len(nw_lst)):
        if nw_lst[i] == search:
            nw_lst[i] = replace
    return (nw_lst)
