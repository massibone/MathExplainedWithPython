'''
 verificare se la matrice A2 può essere ottenuta dalla matrice A1 mediante una trasformazione lineare definita dalla matrice di trasformazione M ( (2,1, -1)
'''
import numpy as np

# Definisci le matrici A1 e A2
A1 = np.array([[1, 1, 3], [2, 1, 0], [0, -2, -1]])
A2 = np.array([[1, 1, 3], [1, 0, -3], [0, -2, -1]])

# Definisci la matrice di trasformazione M
M = np.array([[2, 1, -1], [0, 1, 0], [0, 0, 1]])

# Calcola il risultato della trasformazione di A1 tramite M
result = np.dot(M, A1)

# Verifica se il risultato è uguale a A2
if np.array_equal(result, A2):
    print("A2 è ottenuta da A1 tramite la trasformazione M.")
else:
    print("A2 non è ottenuta da A1 tramite la trasformazione M.")
