#!/usr/bin/python3
# 101-stats.py
# Anas Jellloul
"""Reads input and computes metrics."""


def print_stats(size, status_codes):
    """Print _ metrics.

    Args:
        size (int): accumalted size.
        status_codes (dict): count status code.
    """
    print("File size: {}".format(size))
    for ky in sorted(status_codes):
        print("{}: {}".format(ky, status_codes[ky]))

if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    code_val = ['200', '301', '400', '401', '403', '404', '405', '500']
    cnt = 0

    try:
        for ln in sys.stdin:
            if cnt == 10:
                print_stats(size, status_codes)
                cnt = 1
            else:
                cnt += 1

            ln = ln.split()

            try:
                size += int(ln[-1])
            except (IndexError, ValueError):
                pass

            try:
                if ln[-2] in code_val:
                    if status_codes.get(ln[-2], -1) == -1:
                        status_codes[ln[-2]] = 1
                    else:
                        status_codes[ln[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
