'''
per matrici 3x3
regola di Sarrus:

A = [[1, -2, -1],
[0, 3, 2],
[1, 1, -4]]

det(A) = (1 * 3 * (-4)) + (-2 * 2 * 1) + (-1 * 0 * 1) - ((-1) * 3 * 1) - (1 * 2 * (-4)) - (-2 * 0 * (-1))

det(A) = -12 - 4 + 0 + 3 + 8 + 0

det(A) = -15
'''

import numpy as np

# Definizione della nuova matrice
B = np.array([[1, -2, -1],
              [0, 3, 2],
              [1, 1, -4]])

# Calcolo del determinante di B
det_B = np.linalg.det(B)

# Stampa del risultato
print(det_B)  # Output: -15.0


