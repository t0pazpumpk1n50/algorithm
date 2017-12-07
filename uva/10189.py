def neighbors(r, c, h, w):
    for r2 in (r-1, r, r+1):
        for c2 in (c-1, c, c+1):
            if r2 == r and c2 == c:
                continue
            if c2 < 0 or r2 < 0 or c2 >= w or r2 >= h:
                continue
            yield r2, c2


i = 0
while True:
    h, w = [int(x) for x in input().split()]
    if h == 0 and w == 0:
        break

    print(end='\n' if i > 0 else '')

    F = [bytearray(input().encode()) for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if F[r][c] == ord('.'):
                t = sum(1 for r2, c2 in neighbors(r, c, h, w) if F[r2][c2] == ord('*'))
                F[r][c] = t + ord('0')

    i += 1
    print('Field #%s:' % i)
    print(b'\n'.join(F).decode())

