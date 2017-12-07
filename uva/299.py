m = int(input())
for _ in range(m):
    n = int(input())
    A = [int(x) for x in input().split()]
    r = 0
    for i in range(n):
        for j in range(i + 1, n):
            if A[i] > A[j]:
                r += 1
    print('Optimal train swapping takes %s swaps.' % r)

