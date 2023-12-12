
import numpy as np

# Definisci la matrice A
A = np.array([[1, 0, 3, 0],
              [0, 1, 0, 3],
              [2, 0, 1, 0],
              [0, 2, 0, 1]])

# Calcola la decomposizione LU di A
P, L, U = scipy.linalg.lu(A)

# Calcola l'inversa di A utilizzando la decomposizione LU
A_inv = np.linalg.inv(U) @ np.linalg.inv(L) @ np.linalg.inv(P)

print(A_inv)
