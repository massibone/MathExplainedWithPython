'''
A antisimmetrica= 1/2(A-A**T)
A**t è la trasposta ( basta scambiare le righe con le colonne Attenzione alla simmetrica )
Risultato:
[[ 0. -1. -2.]
 [ 1.  0. -1.]
 [ 2.  1.  0.]]
'''

import numpy as np

# Definisci la matrice A con tipi di dati appropriati (ad esempio, float)
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)

# Calcola la trasposta di A
A_trasposta = np.transpose(A)

# Calcola la matrice antisimmetrica
A_antisimmetrica = 0.5 * (A - A_trasposta)

# Stampa la matrice antisimmetrica
print("Matrice antisimmetrica A_antisimmetrica:")
print(A_antisimmetrica)
