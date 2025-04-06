import numpy as np

def householder(A, b):
    A = A.astype(float)
    b = b.astype(float)
    m, n = A.shape

    for k in range(n):
        x = A[k:, k]
        e = np.zeros_like(x)
        e[0] = np.linalg.norm(x) * (-1 if x[0] < 0 else 1)
        u = x + e
        v = u / np.linalg.norm(u)

        A[k:, k:] -= 2.0 * np.outer(v, v @ A[k:, k:])
        b[k:] -= 2.0 * v * (v @ b[k:])


    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - A[i, i + 1:] @ x[i + 1:]) / A[i, i]
    return x
