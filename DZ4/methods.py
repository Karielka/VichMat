from data_input import f

def central_rectangles(a, b, n):
    """ Метод центральных прямоугольников. """

    h = (b - a) / n
    result = 0
    for i in range(n):
        xi = a + h * (i + 0.5)
        result += f(xi)
    return result * h

def trapezoidal(a, b, n):
    """ Метод трапеций. """

    h = (b - a) / n
    result = (f(a) + f(b)) / 2
    for i in range(1, n):
        xi = a + h * i
        result += f(xi)
    return result * h

def runge_trapezoidal(a, b, eps):
    """ Метод трапеций с автоматическим выбором шага по правилу Рунге. """

    n = 2
    I_n = trapezoidal(a, b, n)
    n *= 2
    I_2n = trapezoidal(a, b, n)
    while abs(I_n - I_2n) / 3 > eps:
        n *= 2
        I_n = I_2n
        I_2n = trapezoidal(a, b, n)
    return I_2n, n

def simpson(a, b, n):
    """ Метод Симпсона. """

    if n % 2 != 0:
        n += 1  # Симпсон требует чётное число отрезков
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n, 2):
        result += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        result += 2 * f(a + i * h)
    return result * h / 3

def runge_simpson(a, b, eps):
    """ Метод Симпсона с автоматическим выбором шага по правилу Рунге. """

    n = 2
    I_n = simpson(a, b, n)
    n *= 2
    I_2n = simpson(a, b, n)
    while abs(I_n - I_2n) / 15 > eps:
        n *= 2
        I_n = I_2n
        I_2n = simpson(a, b, n)
    return I_2n, n
