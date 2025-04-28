from data_input import get_parameters, exact_integral
from methods import (
    central_rectangles,
    trapezoidal,
    runge_trapezoidal,
    runge_simpson,
)

def main():
    a, b, eps = get_parameters()
    exact = exact_integral()

    print(f"Точное значение интеграла: {exact:.6f}\n")

    # Центральные прямоугольники
    n = 2
    while True:
        integral = central_rectangles(a, b, n)
        next_integral = central_rectangles(a, b, n * 2)
        if abs(integral - next_integral) / 3 <= eps:
            break
        n *= 2
    print(f"Метод центральных прямоугольников: {next_integral:.6f} при n = {n * 2}")

    # Метод трапеций с шагом по второй производной
    n = 2
    while True:
        integral = trapezoidal(a, b, n)
        next_integral = trapezoidal(a, b, n * 2)
        if abs(integral - next_integral) / 3 <= eps:
            break
        n *= 2
    print(f"Метод трапеций: {next_integral:.6f} при n = {n * 2}")

    # Метод трапеций с Рунге
    integral_runge, n_runge = runge_trapezoidal(a, b, eps)
    print(f"Метод трапеций с правилом Рунге: {integral_runge:.6f} при n = {n_runge}")

    # Метод Симпсона с Рунге
    integral_simpson, n_simpson = runge_simpson(a, b, eps)
    print(f"Метод Симпсона с правилом Рунге: {integral_simpson:.6f} при n = {n_simpson}")

    print("\nСравнение:")
    print(f"Абсолютная ошибка центральных прямоугольников: {abs(next_integral - exact):.2e}")
    print(f"Абсолютная ошибка трапеций: {abs(next_integral - exact):.2e}")
    print(f"Абсолютная ошибка трапеций с Рунге: {abs(integral_runge - exact):.2e}")
    print(f"Абсолютная ошибка Симпсона с Рунге: {abs(integral_simpson - exact):.2e}")

if __name__ == "__main__":
    main()
