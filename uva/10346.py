import sys

for line in sys.stdin:
    n, k = map(int, line.split())
    r = 0
    while n >= k:
        r += n - (n % k)
        n = n % k + n // k
    r += n
    print(r)

