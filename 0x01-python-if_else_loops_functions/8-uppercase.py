#!/usr/bin/python3
def uppercase(str):
    for ix in str:
        if ord(ix) >= 97 and ord(ix) <= 122:
            ch = chr(ord(ix) - 32)
        else:
            ch = ix
        print("{:s}".format(ch), end='')
    print('')
