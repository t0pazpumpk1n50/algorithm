import sys

all = sys.stdin.read().split()
n = int(all[0])
A = [int(x) for x in all[1:]]
A = [A[x:x+n] for x in range(0, len(A), n)]

H = [[0 for _ in range(n)] for _ in range(n)]

m = 0
for w in range(0, n):  # w == 0 means 1 column, w == 1 means two columns

    # calculate the sum of the horizontal lines of width w, its the basis of further calculation
    for x in range(n - w):
        for y in range(n):
            if w == 0:
                H[x][y] = A[y][x]
            else:
                H[x][y] += A[y][x + w]

    for x in range(n - w):
        s = 0
        for y in range (n):
            if s < 0:
                s = H[x][y]
            else:
                s += H[x][y]
            m = max(m, s)

print(m)

