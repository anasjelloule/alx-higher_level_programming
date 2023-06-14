#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
     return(list(map(lambda ac: list(map(lambda ax: ax ** 2, ac)), matrix)))
