import sys
import bisect

for line in sys.stdin:
    w, h = map(int, line.split())
    print(w * h - 1)
