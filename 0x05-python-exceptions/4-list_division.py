#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nwlst = []
    for x in range(list_length):
        rslt = 0
        try:
            rslt = my_list_1[x] / my_list_2[x]
        except IndexError:
            print("{}".format("out of range"))
        except (ValueError, TypeError):
            print("{}".format("wrong type"))
        except ZeroDivisionError:
            print("{}".format("division by 0"))
        finally:
            nwlst.append(rslt or 0)
    return(nwlst)
