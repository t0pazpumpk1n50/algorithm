n = int(input())
for i in range(n):
    a, b = int(input()), int(input())
    if a % 2 == 0:
        a += 1
    if b % 2 == 0:
        b -= 1
    r = (b + a) / 2 * ((b - a) / 2 + 1)
    print('Case %s: %d' % (i + 1, r))
