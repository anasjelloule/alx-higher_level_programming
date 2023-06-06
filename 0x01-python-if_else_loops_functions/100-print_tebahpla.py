#!/usr/bin/python3
for ix in range(122, 96, -1):
    if ix % 2 == 0:
        ch = chr(ix)
    else:
        ch = chr(ix - 32)
    print("{:s}".format(ch), end='')
