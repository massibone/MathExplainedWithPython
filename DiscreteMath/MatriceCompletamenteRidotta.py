'''
Una matrice si dice completamente ridotta secondo la forma di Gauss-Jordan se soddisfa le seguenti condizioni:

Ogni colonna contenente un elemento pivot (il primo elemento non nullo in ogni colonna) deve contenere solo zeri in tutte le posizioni al di fuori del pivot.
Ogni riga contenente un elemento pivot deve contenere solo zeri in tutte le posizioni al di fuori del pivot.
Tutte le righe o colonne nulle devono apparire in basso o a destra della matrice.
Per la matrice A data:
[[ 1  0  0  0]
 [ 0  0 -1  0]
 [ 0  2  0  2]
 [ 0  0  0  0]]
Possiamo vedere che:

La prima colonna contiene un elemento pivot (1) e contiene solo zeri al di fuori del pivot.
La terza colonna contiene un elemento pivot (-1) e contiene solo zeri al di fuori del pivot.
La seconda colonna contiene un elemento pivot (2) e contiene solo zeri al di fuori del pivot.
La quarta colonna è nullo.
Inoltre, tutte le righe nulle appaiono in basso della matrice.

Quindi, la matrice A è completamente ridotta secondo la forma di Gauss-Jordan, con la sequenza di colonne pivot (1,2,3) e la sequenza di righe pivot (1,2,3).

Ricorda che la forma completamente ridotta rappresenta una forma finale di eliminazione gaussiana che semplifica ulteriormente la matrice a scopi di calcoli e analisi.
'''
import numpy as np

# Definisci la matrice A
A = np.array([[1, 0, 0, 0], [0, 0, -1, 0], [0, 2, 0, 2], [0, 0, 0, 0]])

# Riduci A alla forma di Gauss-Jordan (forma completamente ridotta)
rows, cols = A.shape
row_index = 0
col_index = 0

while row_index < rows and col_index < cols:
    # Trova la riga con il massimo elemento nella colonna corrente
    max_row = np.argmax(np.abs(A[row_index:, col_index])) + row_index
    
    # Scambia le righe in modo che il massimo elemento sia sulla diagonale
    A[[row_index, max_row]] = A[[max_row, row_index]
 
