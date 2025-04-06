def newton(f, df, x0, eps, max_iter=1000):
    x = x0
    iterations = 0
    while iterations < max_iter:
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            raise ZeroDivisionError("Производная равна нулю.")
        x_new = x - fx / dfx
        if abs(x_new - x) < eps:
            return x_new, iterations
        x = x_new
        iterations += 1
    raise RuntimeError("Метод Ньютона не сошелся.")
