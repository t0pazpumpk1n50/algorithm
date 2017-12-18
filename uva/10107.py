import sys
import bisect

a = []
for line in sys.stdin:
    x = int(line)
    bisect.insort(a, x)
    n = len(a)
    if n % 2 == 0:
        print((a[n//2 - 1] + a[n//2]) // 2)
    else:
        print(a[n//2])

