#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as errs:
        print("Exception:", errs, file=sys.stderr)
        return None
