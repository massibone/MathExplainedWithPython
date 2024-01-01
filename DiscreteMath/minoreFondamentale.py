import numpy as np

# Definisci la matrice A
A = np.array([[-2, 3, 1, -5],
              [1, -1, 0, 2],
              [0, 2, 2, -2],
              [-1, 3, 2, -4]])


# Seleziona le righe e le colonne desiderate per il minore fondamentale
sottomatrice = A[[1, 2], 2:4]
