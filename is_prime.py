def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    x = 5
    inc = 2
    while x * x <= n:
        if n % x == 0:
            return False
        x += inc
        inc = 6 - inc

    return True


for i in range(1, 100):
    if is_prime(i):
        print(i)

