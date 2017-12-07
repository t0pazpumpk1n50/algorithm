n = int(input())

for i in range(n):
    A = [int(x) for x in input().split()]
    print('Case %s: %s' % (i + 1, sorted(A)[1]))
    
