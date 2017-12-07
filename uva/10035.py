import sys

for line in sys.stdin:
    a, b = line.split()
    if a == '0' and b == '0':
        break

    if len(a) < len(b):
        a, b = b, a
    b = b.rjust(len(a), '0')

    n = 0
    carry = 0
    for x, y in reversed(list(zip(a, b))):
        t = carry + ord(x) - ord('0') + ord(y) - ord('0')
        carry = 0
        if t >= 10:
            n += 1
            carry = 1
    print('No carry operation.' if n == 0 else '1 carry operation.' if n == 1 else ('%s carry operations.' % n))
