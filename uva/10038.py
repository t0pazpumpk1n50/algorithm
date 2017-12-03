import sys


def is_jolly(A):
    n = len(A)
    if n <= 1:
        return True

    S = [False] * n
    for a, b in zip(A, A[1:]):
        d = abs(a - b)
        if d >= n:
            return False
        S[d] = True
    return all(S[1:])


for line in sys.stdin:
    A = [int(x) for x in line.split()[1:]]
    print('Jolly' if is_jolly(A) else 'Not jolly')

