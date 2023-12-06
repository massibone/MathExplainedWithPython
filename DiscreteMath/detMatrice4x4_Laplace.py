import numpy as np

# Definisci la matrice
A = np.array([[3, -2, 4, 0],
              [2, 1, 1/2, 3],
              [0, 1, 0, -2],
              [0, -1, 1, 1]])

# Calcola il determinante
det_A = np.linalg.det(A)

# Stampalo
print(f"Il determinante della matrice A è: {det_A}")
