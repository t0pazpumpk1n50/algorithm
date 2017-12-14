t = int(input())
for i in range(t):
    A = [int(x) for x in input().split()[1:]]
    print('Case %s: %s' % (i + 1, max(A)))
    
