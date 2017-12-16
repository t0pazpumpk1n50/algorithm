n = int(input())
s = ''.join([input() for _ in range(n)])
count = {}
for c in s:
    if c.isalpha():
        count[c.upper()] = count.get(c.upper(), 0) + 1
for k, v in sorted(count.items(), key=lambda x: (-x[1], x[0])):
    print(k, v)
