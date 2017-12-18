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


while True:
    n = int(input())
    if n == 0:
        break

    for i in range(n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            print('%s = %s + %s' % (n, i, n - i))
            break
    else:
        print("Goldbach's conjecture is wrong.")
