c = int(input())

for _ in range(c):
    A = [int(x) for x in input().split()][1:]
    avg = sum(A) / len(A)
    percentage = sum(1 for x in A if x > avg) * 100 / len(A)
    print('%2.3f%%' % percentage)
