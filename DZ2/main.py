import numpy as np
from math import log

# Уравнение 1
def f1(x):
    return x**4 - 18*x**2 + 6
# Уравнение 2
def f2(x):
    return 5**x - 2*x - 3
def df2(x):
    return 5**x * log(5) - 2
def phi2(x):
    return log(2 * x + 3) / log(5)
def phi_neg(x):
    return (5**x - 3) / 2
def f_neg(x):
    return 5**x - 2*x - 3
def df_neg(x):
    return 5**x * log(5) - 2

from bisect import bisection
from iteration import simple_iteration
from newton import newton

print("Задача 1: Метод бисекций")
x_bisect, it_bisect = bisection(f1, -5, -3, 0.001)
print(f"Корень: {x_bisect:.5f}, итерации: {it_bisect}")
x_bisect, it_bisect = bisection(f1, -1, 0, 0.001)
print(f"Корень: {x_bisect:.5f}, итерации: {it_bisect}")
x_bisect, it_bisect = bisection(f1, 0, 1, 0.001)
print(f"Корень: {x_bisect:.5f}, итерации: {it_bisect}")
x_bisect, it_bisect = bisection(f1, 3, 5, 0.001)
print(f"Корень: {x_bisect:.5f}, итерации: {it_bisect}")

print("\nЗадача 2: Метод простой итерации")
x_iter, it_iter = simple_iteration(phi2, 2.0, 0.0001)
print(f"Корень: {x_iter:.5f}, итерации: {it_iter}")
x_iter2, it_iter2 = simple_iteration(phi_neg, -1.2, 0.0001)
print(f"Корень: {x_iter2:.5f}, итераций: {it_iter2}")

print("\nЗадача 2: Метод Ньютона")
x_newt, it_newt = newton(f2, df2, 2.0, 0.0001)
print(f"Корень: {x_newt:.5f}, итерации: {it_newt}")
x_newt2, it_newt2 = newton(f_neg, df_neg, -1.2, 0.0001)
print(f"Корень: {x_newt2:.5f}, итераций: {it_newt2}")