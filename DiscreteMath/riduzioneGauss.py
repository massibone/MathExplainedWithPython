import numpy as np

# Definisci la matrice A con il tipo di dati float64
A = np.array([[0, 1, 2, -1], [1, 0, 0, -1], [2, 1, 1, -1]], dtype=np.float64)

# Applica l'algoritmo di eliminazione di Gauss
rows, cols = A.shape

for col in range(cols):
    # Trova la prima riga con un pivot non nullo nella colonna corrente
    pivot_row = None
    for row in range(col, rows):
        if A[row, col] != 0:
            pivot_row = row
            break
    
    # Se non ci sono pivot non nulli, passa alla prossima colonna
    if pivot_row is None:
        continue
    
    # Scambia la riga pivot con la riga corrente
    A[[col, pivot_row]] = A[[pivot_row, col]]
    
    # Riduci gli elementi sotto il pivot a zero
    for row in range(col + 1, rows):
        factor = A[row, col] / A[col, col]
        A[row, col:] -= factor * A[col, col:]
        
print("Matrice A ridotta:")
print(A)
