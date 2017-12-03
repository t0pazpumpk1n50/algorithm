import sys
import itertools


def solve(B0, B1, B2):
    r = None
    min_moves = None
    for p in itertools.permutations(range(3)):  # p[i] indicates which color to keep in bin i, e.g. value of 0 means Brown
        moves = B0[p[1]] + B0[p[2]] + B1[p[0]] + B1[p[2]] + B2[p[0]] + B2[p[1]]
        if not min_moves or moves < min_moves:
            min_moves = moves
            r = 'BGC'[p[0]] + 'BGC'[p[1]] + 'BGC'[p[2]]
        elif moves == min_moves:
            r = min(r, 'BGC'[p[0]] + 'BGC'[p[1]] + 'BGC'[p[2]])

    print(r, min_moves)


for line in sys.stdin:
    A = [int(x) for x in line.split()]
    solve(A[0:3], A[3:6], A[6:9])

