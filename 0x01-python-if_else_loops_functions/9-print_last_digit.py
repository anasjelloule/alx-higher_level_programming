#!/usr/bin/python3
def print_last_digit(number):
    anas = abs(number) % 10
    print("{:d}".format(anas), end='')
    return anas
