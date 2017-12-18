while True:
    s = input()
    if s == '0':
        break

    r = 0
    m = 0
    for c in s:
        t = ord(c) - ord('0')
        r = (r + t) << 1
        m += t
    r -= m
    print(r)

