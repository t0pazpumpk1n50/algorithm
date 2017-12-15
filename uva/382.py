import sys


def proper_divisors_sum(n):
    r = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            r += i
    return r


print('PERFECTION OUTPUT')
for n in [int(x) for x in sys.stdin.read().split()]:
    if n == 0:
        break
    s = proper_divisors_sum(n)
    print('%5d  %s' % (n, 'PERFECT' if n == s else 'DEFICIENT' if n > s else 'ABUNDANT'))
print('END OF OUTPUT')

