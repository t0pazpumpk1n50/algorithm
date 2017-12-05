n = int(input())
for _ in range(n):
    m = int(input())
    r = 0
    for _ in range(m):
        s, a, e = [int(x) for x in input().split()]
        r += e * s
    print(r)
