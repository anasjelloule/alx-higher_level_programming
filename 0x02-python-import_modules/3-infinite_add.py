#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    rslt = sum(int(sys.argv[anas]) for anas in range(1, len(sys.argv)))
    print("{}".format(rslt))
