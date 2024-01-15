import numpy as np

# Creare una matrice 5x5 di esempio
A = np.array([
    [2, 1, 0, 3, 5],
    [0, 0, 1, 2, 1],
    [0, 0, 0, 1, 4],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
])

# Eseguire la riduzione a forma normale di Gauss
rref_A, pivot_columns = np.linalg.qr(A, mode='r')

print("Matrice originale:\n", A)
print("\nMatrice ridotta a forma normale di Gauss:\n", rref_A)
print("\nColonne di pivot:", pivot_columns)
'''
RISULTATO:
2 1 0 3 5
0 0 1 2 1
0 0 0 1 4
0 0 0 0 0
0 0 0 0 0
Qui, i pivot sono gli elementi 2, 1, 1. I pivot sono nella colonna 1, 2 e 4.
'''
