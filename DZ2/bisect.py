def bisection(f, a, b, eps):
    if f(a) * f(b) >= 0:
        raise ValueError("Неправильный выбор интервала.")
    iterations = 0
    while (b - a) / 2 > eps:
        c = (a + b) / 2
        if f(c) == 0:
            return c, iterations
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterations += 1
    return (a + b) / 2, iterations
