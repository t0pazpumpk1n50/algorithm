
n = int(input())
for _ in range(n):
    s = input()
    a = int(s) + int(s[::-1])
    r = 1
    while str(a) != str(a)[::-1]:
        a += int(str(a)[::-1])
        r += 1
    print(r, a)

