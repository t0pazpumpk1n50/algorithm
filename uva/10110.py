def sqrt(n):
    x0 = n // 2
    while True:
        better = int((x0 + n / x0) * 0.5)
        if x0 == better:
            break
        x0 = better
    return x0

while True:
    n = int(input())
    if n == 0:
        break
    r = sqrt(n)
    print('yes' if r * r == n else 'no')

