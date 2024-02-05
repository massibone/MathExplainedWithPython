'''
La matrice di trasformazione M è ottenuta dall'operazione che trasforma la matrice A1 nella matrice A2. 
Per calcolare questa matrice di trasformazione, è possibile risolvere il sistema di equazioni lineari:

M⋅A1=A2

In altre parole, moltiplicando la matrice A1 per la matrice di trasformazione M, otteniamo la matrice A2.
'''
import numpy as np

# Definisci le matrici A1 e A2
A1 = np.array([[1, 1, 3], [2, 1, 0], [0, -2, -1]])
A2 = np.array([[1, 1, 3], [1, 0, -3], [0, -2, -1]])

# Risolvi il sistema di equazioni lineari per ottenere M
M = np.linalg.solve(A1, A2)

print("Matrice di trasformazione M:")
print(M)
