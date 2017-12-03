import sys
import functools


@functools.lru_cache(None)
def cycle_length(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return cycle_length(n / 2) + 1
    else:
        return cycle_length((3 * n + 1) / 2) + 2


for line in sys.stdin:
    i, j = [int(x) for x in line.split()]
    m = 0
    for k in range(min(i, j), max(i, j) + 1):
        m = max(m, cycle_length(k))
    print(i, j, m, sep=' ')
