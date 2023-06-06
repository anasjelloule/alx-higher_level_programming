#!/usr/bin/python3
def fizzbuzz():
    for ix in range(1, 101):
        anas = ""
        if(xi % 3 == 0):
            anas += "Fizz"
        if(ix % 5 == 0):
            anas += "Buzz"
        print("{}".format(anas) or "{}".format(ix), end='')
        print(" ", end='')
