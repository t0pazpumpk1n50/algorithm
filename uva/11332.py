import sys


def g(n):
    if n < 10:
        return n
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return g(sum)


for line in sys.stdin:
    n = int(line)
    if n == 0:
        break
    print(g(n))
