import numpy as np

# Definire la matrice
A = np.array([
    [0, 1, 3, -1, 0],
    [0, 0, 0, 2, 0],
    [0, 0, 0, 1, 1]
])

# Eseguire la riduzione a forma normale di Gauss
rref_A, pivot_columns = np.linalg.qr(A, mode='r')

# Verificare se la matrice ridotta è a scalini
is_rref_a_stairs = np.all(np.tril(rref_A, k=-1) == 0)

print("Matrice originale:\n", A)
print("\nMatrice ridotta a forma normale di Gauss:\n", rref_A)
print("\nLa matrice è a scalini:", is_rref_a_stairs)
