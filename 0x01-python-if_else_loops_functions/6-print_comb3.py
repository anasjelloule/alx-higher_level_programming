#!/usr/bin/python3
for ix in range(10):
    for jx in range(10):
        if(ix is 8 and jx is 9):
            print("{}".format(str(ix) + str(jx)))
        elif(jx > ix):
            print("{}".format(str(ix) + str(jx)) + ", ", end="")
