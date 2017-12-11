while True:
    n = int(input())
    if n == 0:
        break
    if n <= 101:
        r = 91
    else:
        r = n - 10
    print('f91(%s) = %s' % (n, r))


