def simple_iteration(phi, x0, eps, max_iter=1000):
    x_prev = x0
    iterations = 0
    while iterations < max_iter:
        x_next = phi(x_prev)
        if abs(x_next - x_prev) < eps:
            return x_next, iterations
        x_prev = x_next
        iterations += 1
    raise RuntimeError("Метод простой итерации не сошелся.")
