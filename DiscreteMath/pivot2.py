import numpy as np

# Definire la matrice
A = np.array([
    [1, 2, 0, 0],
    [0, -1, 0, 1],
    [0, 0, 0, 3]
])

# Eseguire la riduzione a forma normale di Gauss
rref_A, pivot_columns = np.linalg.qr(A, mode='r')

print("Matrice originale:\n", A)
print("\nMatrice ridotta a forma normale di Gauss:\n", rref_A)
print("\nColonne di pivot:", pivot_columns)
'''
la matrice ridotta è:
1 2 0 0
0 -1 0 1
0 0 0 3
in questo caso i pivot son (1,-1,3)
'''
