'''
un programma python che dette B e A la matrice completa ed incompleta, risulta rk(B) = rk(A) = 2 


'''

import numpy as np

# Matrice dei coefficienti A (matrice incompleta)
A = np.array([[1, 2, 3],
              [2, 4, 6],
              [3, 6, 9]])

# Matrice completa estesa B
B = np.array([[1, 2, 3, 1],
              [2, 4, 6, 2],
              [3, 6, 9, 3]])

# Calcola il rango di A e B
rank_A = np.linalg.matrix_rank(A)
rank_B = np.linalg.matrix_rank(B)

# Verifica se rk(B) = rk(A) = 2
if rank_B == 2 and rank_A == 2:
    print("rk(B) = 2 e rk(A) = 2. Le equazioni sono linearmente indipendenti.")
else:
    print("Le equazioni non soddisfano rk(B) = 2 e rk(A) = 2.")
