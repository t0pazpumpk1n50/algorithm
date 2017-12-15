n = int(input())
for _ in range(n):
    A = sorted([int(x) for x in input().split()[1:]])
    r = A[len(A)//2]
    print(sum(abs(x - r) for x in A))
