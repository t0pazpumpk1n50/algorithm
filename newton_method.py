def newton_method(f, df, x0, e):
    while True:
        if abs(f(x0)) <= e:
            return x0
        x0 = x0 - f(x0) / df(x0)


f = lambda x: 3 * x**3 + 5 * x**2 - 2 * x + 6
df = lambda x: 9 * x**2 + 10 * x - 2
print(newton_method(f, df, 10, 0.001))

