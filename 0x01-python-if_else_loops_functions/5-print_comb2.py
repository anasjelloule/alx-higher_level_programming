#!/usr/bin/python3
for an in range(0, 100):
    if an != 99:
        print("{:02d}, ".format(an), end='')
    else:
        print("{:02d}".format(an))
