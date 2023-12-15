'''
Una matrice permutabile è una matrice quadrata che può essere riorganizzata (permutata) attraverso scambi di righe e colonne in modo tale da ottenere una matrice con una particolare struttura.
'''

import numpy as np

# Creazione di una matrice di permutazione
n = 4  # Dimensione della matrice
perm_matrix = np.eye(n)  # Matrice identità di dimensione n

# Scambio di righe per ottenere una matrice permutabile
perm_matrix[[1, 2]] = perm_matrix[[2, 1]]

# Creazione di una matrice diagonale
diagonal_matrix = np.diag([1, 2, 3, 4])  # Una matrice diagonale arbitraria

# Calcolo della matrice permutabile
permutable_matrix = np.dot(np.dot(perm_matrix, diagonal_matrix), np.linalg.inv(perm_matrix))

print("Matrice di permutazione:")
print(perm_matrix)

print("\nMatrice diagonale:")
print(diagonal_matrix)

print("\nMatrice permutabile:")
print(permutable_matrix)

'''
Matrice di permutazione:
[[1. 0. 0. 0.] 
 [0. 0. 1. 0.] 
 [0. 1. 0. 0.] 
 [0. 0. 0. 1.]]

Matrice diagonale:
[[1 0 0 0]
 [0 2 0 0]
 [0 0 3 0]
 [0 0 0 4]]

Matrice permutabile:
[[1. 0. 0. 0.]
 [0. 3. 0. 0.]
 [0. 0. 2. 0.]
 [0. 0. 0. 4.]]
'''
