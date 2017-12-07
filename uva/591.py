i = 1
while True:
    n = int(input())
    if n == 0:
        break

    A = [int(x) for x in input().split()]
    avg = sum(A) // len(A)
    print('Set #%s' % i)
    print('The minimum number of moves is %s.\n' % sum(x - avg for x in A if x > avg))
    i += 1
