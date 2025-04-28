import math

def f(x):
    """Интегрируемая функция."""
    return math.sin(x) ** 3

def exact_integral():
    """Точное значение интеграла по формуле Ньютона-Лейбница."""
    # Интеграл sin^3(x) dx можно взять аналитически:
    # sin^3(x) = (3 sin(x) - sin(3x)) / 4
    # => интеграл = ( -3 cos(x) + cos(3x)/3 ) / 4 + C
    a = 0
    b = math.pi / 2

    def F(x):
        return (-3 * math.cos(x) + math.cos(3 * x) / 3) / 4

    return F(b) - F(a)

def get_parameters():
    """Возвращает параметры интегрирования."""
    a = 0
    b = math.pi / 2
    eps = 1e-3
    return a, b, eps
