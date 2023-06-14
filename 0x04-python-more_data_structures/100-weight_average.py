#!/usr/bin/python3
def weight_average(my_list=[]):
    cfs = 0
    sz = 0

    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0

    for ix in my_list:
        cfs += ix[0] * ix[1]
        sz += ix[1]

    return cfs / sz
