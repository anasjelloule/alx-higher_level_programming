#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda ac: list(map(lambda ay: ay ** 2, ac[:])), matrix)))
