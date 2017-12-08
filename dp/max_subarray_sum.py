A = [int(x) for x in input().split()]
m = float('-inf')  # max ever
f = 0  # max ending here
for n in A:
    if f < 0:
        f = n
    else:
        f += n
    m = max(f, m)

