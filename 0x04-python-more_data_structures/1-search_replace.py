#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nw_lst=[]
    for i in my_list:
        if i==search:
            nw_lst.append(replace)
            continue
        nw_lst.append(i)
    return nw_lst
