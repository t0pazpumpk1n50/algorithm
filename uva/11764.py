n = int(input())
for i in range(n):
    input()
    a = [int(x) for x in input().split()]
    h, l = 0, 0
    for x, y in zip(a, a[1:]):
        if x > y:
            l += 1
        elif x < y:
            h += 1
    print('Case %s: %s %s' % (i + 1, h, l))


