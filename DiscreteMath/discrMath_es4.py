
'''
trovare dato 3 matrici con valori x e y nella matrice X che rispetti questa equazione

(trasposta A   A^t) * X = B
'''

import numpy as np

# Definizione delle matrici A e B (2x2)
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Definizione della matrice X con valori sconosciuti x e y
X = np.array([[1, 2], [3, 4]])  # Inizializzazione con valori a caso

# Calcolo della trasposta di A
A_transpose = A.T

# Risoluzione per la matrice X
X_solution = np.dot(np.linalg.inv(A_transpose), B)

# Estrazione dei valori x e y dalla matrice X
x_solution, y_solution = X_solution[0, 0], X_solution[0, 1]

# Stampa dei risultati
print("Matrice A:\n", A)
print("Matrice B:\n", B)
print("Trasposta di A:\n", A_transpose)
print("Soluzione per la matrice X:\n", X_solution)
print("Valore x:", x_solution)
print("Valore y:", y_solution)
