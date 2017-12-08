import sys


def binary_search(n, p, start, stop):
    if start == stop:
        return None

    middle = start + (stop - start) // 2
    t = middle ** n
    if t == p:
        return middle
    elif t < p:
        return binary_search(n, p, middle + 1, stop)
    else:
        return binary_search(n, p, start, middle)


def nth_root(n, p):
    if n == 1:
        return p
    if p == 1:
        return 1

    shifts = 0
    t = 1
    while t <= p:
        t <<= 1
        shifts += 1

    shifts = (shifts - 1) // n
    start = 1 << shifts
    stop = start << 1

    return binary_search(n, p, start, stop)


try:
    while True:
        n, p = [int(input()) for _ in range(2)]
        print(nth_root(n, p))

except EOFError:
    pass
