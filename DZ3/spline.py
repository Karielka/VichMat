import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline
from custom_spline import NaturalCubicSpline
from data_input import get_spline_function_and_range

def build_cubic_spline():
    n, (a, b), f  = get_spline_function_and_range()
    xi = np.linspace(a, b, n)
    yi = [f(x) for x in xi]

    spline = CubicSpline(xi, yi)

    # для отрисовки
    x_dense = np.linspace(a, b, n)
    x_exact = np.linspace(a, b, 500)
    y_dense = spline(x_dense)
    y_exact = [f(x) for x in x_exact]

    # Вывод значений в консоль (бонусом)
    print(f"{'x':>10} {'Spline(x)':>15} {'Exact f(x)':>15} {'|Error|':>10}")
    print("-" * 55)
    for x_val, spline_val, exact_val in zip(x_dense, y_dense, y_exact):
        error = abs(spline_val - exact_val)
        print(f"{x_val:10.5f} {spline_val:15.5f} {exact_val:15.5f} {error:10.5e}")


    plt.figure(figsize=(10, 6))
    plt.plot(x_exact, y_exact, label="Точная функция", linestyle="--", color='green')
    plt.plot(x_dense, y_dense, label="Кубический сплайн", color='blue')
    plt.scatter(xi, yi, color='red', label="Узлы интерполяции")
    plt.title("Интерполяция Кубическим Сплайном")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    build_cubic_spline()
