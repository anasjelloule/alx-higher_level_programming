#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        mx = my_list[0]
        for elm in my_list:
            if elm > mx:
                mx = elm
        return mx
