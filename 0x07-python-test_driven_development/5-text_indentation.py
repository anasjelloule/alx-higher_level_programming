#!/usr/bin/python3
"""Defines a text-indentation FC"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    bc = 0
    for idx, vl in enumerate(text):
        if vl in '?:.':
            print(text[bc:idx + 1].strip() + '\n')
            bc = idx + 1
    if not bc:
        print(text, end='')
    elif bc is not len(text):
        print(text[bc:idx + 1].strip(), end='')
