def nth_ugly_num(n):
    if n == 1:
        return 1

    P = {2: 0, 3: 0, 5: 0}  # positions of next potential factors in R for 2, 3 and 5
    R = [1]  # the ugly num sequence

    for _ in range(n - 1):
        u, x = min((R[P[x]] * x, x) for x in (2, 3, 5))
        R.append(u)

        for x in (2, 3, 5):
            if x * R[P[x]] <= u:
                P[x] += 1
    return R[-1]

print("The 1500'th ugly number is %s." % nth_ugly_num(1500))
