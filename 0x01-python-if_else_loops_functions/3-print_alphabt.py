#!/usr/bin/python3
for ch in range(97, 123):
    if (ch == 113 or ch == 101):
        continue
    print("{:c}".format(ch), end='')
