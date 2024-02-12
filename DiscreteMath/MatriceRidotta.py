'''
La notazione "(1,3) ridotta" si riferisce a una particolare forma di rappresentazione di una matrice nota come "forma di Gauss-Jordan" o "forma normale ridotta a scalini". In questa forma, la matrice viene trasformata in modo che abbia zero in tutte le righe sotto il primo elemento non nullo di ciascuna colonna.
'''
import numpy as np

# Definisci la matrice A
A = np.array([[0, 0, 1], [-1, 1, 0], [1, 1, 0]])

# Riduci A alla forma di Gauss-Jordan
A_ridotta = np.zeros_like(A, dtype=float)

rows, cols = A.shape
row_index = 0

for col_index in range(cols):
    # Trova la riga con il massimo elemento in valore assoluto nella colonna corrente
    max_row = np.argmax(np.abs(A[row_index:, col_index])) + row_index
    
    # Scambia le righe in modo che il massimo elemento sia sulla diagonale
    A[[row_index, max_row]] = A[[max_row, row_index]]
    
    # Riduci a zero gli elementi sotto la diagonale
    A_ridotta[row_index, :] = A[row_index, :] / A[row_index, col_index]
    for i in range(rows):
        if i != row_index:
            A_ridotta[i, :] = A[i, :] - A[i, col_index] * A_ridotta[row_index, :]
    
    row_index += 1

print("Matrice A ridotta alla forma (1,3):")
print(A_ridotta)





