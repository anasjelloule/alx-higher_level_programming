#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
        if(matrix):
                return ([list(map(lambda ac: ac * ac, rw)) for rw in matrix])
