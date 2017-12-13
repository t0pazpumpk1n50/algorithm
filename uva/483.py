import sys

for line in sys.stdin:
    print(' '.join(w[::-1] for w in line.split()))
