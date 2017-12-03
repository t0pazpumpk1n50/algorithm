import sys

for line in sys.stdin:
    v, t = [int(x) for x in line.split()]
    if t == 0:
        print(0)
    else:
        a = v / t
        d = a * (2 * t) ** 2 / 2
        print(int(round(d)))
