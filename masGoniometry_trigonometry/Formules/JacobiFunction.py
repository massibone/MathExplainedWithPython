import numpy as np

# Define the system of linear equations
A = np.array([[4, -1, 0], [-1, 4, -1], [0, -1, 4]])
b = np.array([5, 0, 5])

# Define the Jacobi function
def jacobi(A, b, x0, tol=1e-6, max_iter=1000):
    n = len(A)
    x = np.array(x0)
    for k in range(max_iter):
        x_new = np.zeros(n)
        for i in range(n):
            s = sum([A[i, j] * x[j] for j in range(n) if j != i])
            x_new[i] = (b[i] - s) / A[i, i]
            if np.linalg.norm(x_new - x) < tol:
                return x_new
            x = x_new
            print("Warning: jacobi did not converge")

# Solve the system using Jacobi method
x0 = [0, 0, 0]
x = jacobi(A, b, x0)
print(x)