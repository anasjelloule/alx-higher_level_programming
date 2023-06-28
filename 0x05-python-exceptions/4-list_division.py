#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    rslt = []
    try:
        for i in range(list_length):
            try:
                rslt.append(my_list_1[i] / my_list_2[i])
            except ZeroDivisionError:
                rslt.append(0)
                print("division by 0")
            except TypeError:
                rslt.append(0)
                print("wrong type")
            except IndexError:
                rslt.append(0)
                print("out of range")
    finally:
        return rslt
