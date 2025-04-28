import matplotlib.pyplot as plt
import numpy as np
from data_input import get_tabulated_points

def lagrange_polynomial(x, xi, yi):
    """Вычисляет значение полинома Лагранжа в точке x."""
    n = len(xi)
    result = 0
    for i in range(n):
        term = yi[i]
        for j in range(n):
            if i != j:
                term *= (x - xi[j]) / (xi[i] - xi[j])
        result += term
    return result

def plot_lagrange():
    xi, yi = get_tabulated_points()
    x = np.linspace(min(xi), max(xi), 500)
    y = [lagrange_polynomial(xi_val, xi, yi) for xi_val in x]

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label="Полином Лагранжа", color='blue')
    plt.scatter(xi, yi, color='red', label="Узлы интерполяции")
    plt.title("Интерполяция Полиномом Лагранжа")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    plot_lagrange()
