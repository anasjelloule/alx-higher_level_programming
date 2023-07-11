#!/usr/bin/python3
# Anas Jelloul
"""Impliment Pascal's_Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's_Triangle of n.

    Returns a list(lists(integers representing the triangle)).
    """
    if n <= 0:
        return []

    trgls = [[1]]
    while len(trgls) != n:
        tr_i = trgls[-1]
        _temp = [1]
        for i in range(len(tr_i) - 1):
            _temp.append(tr_i[i] + tr_i[i + 1])
        _temp.append(1)
        trgls.append(_temp)
    return trgls
