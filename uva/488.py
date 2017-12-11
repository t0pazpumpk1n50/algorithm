n = int(input())
for i in range(n):
    print(end='' if i == 0 else '\n')
    input()
    a, f = [int(input()) for _ in range(2)]
    for j in range(f):
        print(end='' if j == 0 else '\n')
        r = list(range(1, a + 1))
        r += r[-2::-1]
        for k in r:
            print(str(k) * k)



