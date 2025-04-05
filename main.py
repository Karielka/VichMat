import numpy as np
from numpy.linalg import norm, inv, cond

from gauss import gauss
from householder import householder
from progonka import progonka

def run_all_methods(A, b, x_exact, label):
    print(f"\n===== {label} =====")
    
    for method_name, solver in [("Метод Гаусса", gauss), ("Метод Хаусхолдера", householder)]:
        x = solver(A.copy(), b.copy())

        r = A @ x - b
        error = x - x_exact

        print(f"\n{method_name}")
        print("x =", x)
        print("1-норма невязки:", norm(r, 1))
        print("∞-норма невязки:", norm(r, np.inf))
        print("1-норма погрешности:", norm(error, 1))
        print("∞-норма погрешности:", norm(error, np.inf))

        relative_error_1 = norm(error, 1) / norm(x_exact, 1)
        relative_error_inf = norm(error, np.inf) / norm(x_exact, np.inf)
        print("Относительная 1-норма погрешности:", relative_error_1)
        print("Относительная ∞-норма погрешности:", relative_error_inf)

    # Обратная матрица и проверка
    A_inv = inv(A)
    I_approx = A_inv @ A
    print("\nОбратная матрица A⁻¹:")
    print(A_inv)
    print(f"Норма (E - A⁻¹A): {norm(np.eye(len(A)) - A_inv @ A):.3e}")
    
    # Обусловленность
    cond_1 = cond(A, 1)
    cond_inf = cond(A, np.inf)
    print(f"cond_1(A): {cond_1:.3e}")
    print(f"cond_inf(A): {cond_inf:.3e}")


    if cond_1 < 100:
        print("➤ Матрица хорошо обусловлена.")
    else:
        print("➤ Матрица плохо обусловлена. Результаты могут быть неточными.")

# ============ Вариант 16 ============

# 1. Хорошо обусловленная система
A1 = np.array([
    [31.2, -1.32, -7.68, 4.09],
    [7.23, -126.0, 7.14, 3.04],
    [9.49, 6.4, 6.0, 8.45],
    [2.68, -3.29, 0.28, 13.4]
])
b1 = np.array([-83.32, 38.9, -56.7, -504.09])
x1_exact = np.array([10, 1, 30, -40])

run_all_methods(A1, b1, x1_exact, "Система 1: Хорошо обусловленная")

# 2. Плохо обусловленная система
A2 = np.array([
    [-27.717, -6.32, 42.652, -0.676],
    [-1332.48, -276.381, 1885.764, -32.496],
    [-222.08, -45.988, 313.841, -5.416],
    [-390.488, -58.284, 416.358, -9.521]
])
b2 = np.array([3.977, -193.092, -33.239, -374.523])
x2_exact = np.array([3, -8, 1, 9])

run_all_methods(A2, b2, x2_exact, "Система 2: Плохо обусловленная")

# -----
print()
print()

# Данные варианта 16
a = np.array([0, 1, 0, 1, 1, -1], dtype=float)  # длина = n-1
c = np.array([103, 124, 91, 59, 72, 111, 93], dtype=float)  # длина = n
b = np.array([0, 1, 0, 0, 1, 1], dtype=float)  # длина = n-1
d = np.array([9, 11, 8, 7, 7, 12, 10], dtype=float)  # длина = n

# Решение методом прогонки
x = progonka(a, c, b, d)

# Собираем A для проверки (только для проверки!)
n = len(c)
A = np.zeros((n, n))
for i in range(n):
    A[i, i] = c[i]
    if i > 0:
        A[i, i - 1] = a[i - 1]
    if i < n - 1:
        A[i, i + 1] = b[i]

# Вычисление невязки
r = A @ x - d

print("Решение методом прогонки:")
print("x =", x)
print("1-норма невязки:", np.linalg.norm(r, 1))
print("∞-норма невязки:", np.linalg.norm(r, np.inf))
