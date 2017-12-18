r = list()
while True:
    s = input()[::-1]
    if s == '0':
        break

    if len(s) > len(r):
        r += [0] * (len(s) - len(r))

    carry = 0
    for i in range(len(r)):
        t = r[i] + (int(s[i]) if i < len(s) else 0) + carry
        r[i] = t % 10
        carry = t // 10
    if carry > 0:
        r.append(carry)

print(''.join(str(x) for x in r[::-1]))

