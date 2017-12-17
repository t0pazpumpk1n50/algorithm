def big_mod(b, p, m):
    if p == 0:
        return 1
    if p % 2 == 1:
        return (big_mod(b, p - 1, m) * b) % m
    else:
        return (big_mod(b, p//2, m) ** 2) % m
    return t


try:
    while True:
        b, p, m = [int(input()) for _ in range(3)]
        b = b % m
        print(big_mod(b, p, m))
        input()
except EOFError:
    pass
