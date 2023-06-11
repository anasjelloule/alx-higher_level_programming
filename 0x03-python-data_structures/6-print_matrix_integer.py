#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rw in matrix:
        for itm in rw:
            print("{:d}".format(itm), end=' ' if itm != rw[-1] else '')
        print()
