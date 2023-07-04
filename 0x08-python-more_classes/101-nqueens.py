#!/usr/bin/python3
"""N queens puzzle is the challenge
"""
import sys


def printBoard(brd):
    if any(1 in x for x in brd):
        print([[idxx, brd[idxx].index(1)] for idxx, val in enumerate(brd)])


def isSafe(rw, sqr, chsbrd, N, dg):
    if chsbrd[rw][sqr]:
        return False
    if sqr - dg >= 0 and chsbrd[rw][sqr - dg]:
        return False
    if sqr + dg < (N) and chsbrd[rw][sqr + dg]:
        return False
    if rw == 0:
        return True
    return isSafe(rw - 1, sqr, chsbrd, N, dg + 1)


def placeSquare(rw, pst, chsbrd, N):
    for sqr in range(pst, N):
        if 1 in chsbrd[rw]:
            return 0
        if not isSafe(rw - 1, sqr, chsbrd, N, 1):
            continue
        chsbrd[rw][sqr] = 1
        return
    return 1


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]

if not str.isdigit(N):
    print("N must be a number")
    sys.exit(1)

N = int(N)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

qun = 0

while qun != N:
    chsbrd = [[0 for x in range(N)] for x in range(N)]
    chsbrd[0][qun] = 1
    ps = 0
    rw = 1
    while rw < N:
        if placeSquare(rw, ps, chsbrd, N):
            rw -= 1
            ps = chsbrd[rw].index(1)
            chsbrd[rw][ps] = 0
            ps += 1
            if not rw:
                break
        else:
            rw += 1
            ps = 0
    printBoard(chsbrd)
    qun += 1
