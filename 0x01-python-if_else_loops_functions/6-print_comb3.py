#!/usr/bin/python3
for ix in range(0, 10):
    for jx in range(ix + 1, 10):
        print("{:d}{:d}".format(ix, jx), end='')
        if (ix != 8 or jx != 9):
            print(", ", end='')
print()
