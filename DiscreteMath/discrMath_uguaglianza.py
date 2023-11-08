import numpy as np

def check_t(t):
    A = np.array([[1, 3], [0, 1]])
    B = np.array([[t, t + 1], [2 - t, t - 1]])

    return np.array_equal(A, B)

# Itera su possibili valori di t
for t in np.linspace(-10, 10, 1000):
    if check_t(t):
        print("Il valore di t che rende vera l'uguaglianza è:", t)
        break
else:
    print("Nessun valore di t rende vera l'uguaglianza.")
