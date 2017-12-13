while True:
    n = int(input())
    if n == 0:
        break
    x0, y0 = map(int, input().split())
    for _ in range(n):
        x, y = map(int, input().split())
        if x == x0 or y == y0:
            print('divisa')
        elif x < x0 and y < y0:
            print('SO')
        elif x < x0 and y > y0:
            print('NO')
        elif x > x0 and y < y0:
            print('SE')
        else:
            print('NE')



