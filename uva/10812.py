n = int(input())
for _ in range(n):
    s, d = [int(x) for x in input().split()]
    if s < d or (s - d) % 2 != 0:
        print('impossible')
    else:
        a = (s + d) // 2
        b = (s - d) // 2
        print(a, b)

