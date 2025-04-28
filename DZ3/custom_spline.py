"""
    Если не в лом, используйте не библиотечный сплайн:)
"""

import numpy as np
from data_input import f

class NaturalCubicSpline:
    def __init__(self, x, y):
        self.n = len(x) - 1
        self.x = x
        self.y = y
        self.h = [x[i+1] - x[i] for i in range(self.n)]

        # Решаем систему для коэффициентов c
        self.a = y
        self.c = self._solve_c()
        self.b = [0] * self.n
        self.d = [0] * self.n

        for i in range(self.n):
            self.d[i] = (self.c[i+1] - self.c[i]) / (3 * self.h[i])
            self.b[i] = (self.a[i+1] - self.a[i]) / self.h[i] - self.h[i] * (self.c[i+1] + 2*self.c[i]) / 3

    def _solve_c(self):
        """Решение трёхдиагональной системы методом прогонки"""
        n = self.n
        A = [0] + [self.h[i-1] for i in range(1, n)]
        B = [2 * (self.h[i-1] + self.h[i]) for i in range(1, n)]
        C = [self.h[i] for i in range(1, n)] + [0]
        F = [0] * (n-1)
        for i in range(1, n):
            F[i-1] = 3 * ((self.a[i+1] - self.a[i]) / self.h[i] - (self.a[i] - self.a[i-1]) / self.h[i-1])

        # Прямой ход
        alpha = [0] * (n-1)
        beta = [0] * (n-1)
        alpha[0] = -C[0] / B[0]
        beta[0] = F[0] / B[0]

        for i in range(1, n-1):
            denom = B[i] + A[i] * alpha[i-1]
            alpha[i] = -C[i] / denom
            beta[i] = (F[i] - A[i] * beta[i-1]) / denom

        # Обратный ход
        c = [0] * (n+1)
        for i in reversed(range(1, n)):
            c[i] = alpha[i-1] * c[i+1] + beta[i-1]
        c[0] = c[n] = 0  # Свободные края

        return c

    def __call__(self, x_val):
        """Вычисляет значение сплайна в точке x_val"""
        # Находим нужный отрезок
        i = self._find_segment(x_val)
        dx = x_val - self.x[i]
        return self.a[i] + self.b[i]*dx + self.c[i]*dx**2 + self.d[i]*dx**3

    def _find_segment(self, x_val):
        """Бинарный поиск интервала"""
        left = 0
        right = self.n
        while left <= right:
            mid = (left + right) // 2
            if self.x[mid] <= x_val <= self.x[mid+1]:
                return mid
            elif x_val < self.x[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return self.n - 1  # если вдруг x_val == x[-1]

