#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args_ = len(sys.argv)
    if(args_ <= 1):
        print("{} arguments.".format(args_ - 1))
    elif(args_ == 2):
        print("{} argument:".format(args_ - 1))
    else:
        print("{} arguments:".format(args_ - 1))
    for x in range(1, args_):
        print("{}: {}".format(x, sys.argv[x]))
