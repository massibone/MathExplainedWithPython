'''
Calcolare la trasposta di una matrice significa scambiare le righe con le colonne. 
A=[ 1 4
​    2 5
    3 6 ]

    la transposta è A**T
    [1 2 3
     4 5 6]

Poiché la matrice data è simmetrica rispetto alla diagonale principale, la sua trasposta è uguale alla matrice stessa.

Quindi, la trasposta della matrice data è:

'''

import numpy as np

# Definisci la matrice A
A = np.array([[1, 'z', 'x'],
              ['z', 2, 0],
              ['x', 0, 3]])

# Calcola la trasposta di A
A_trasposta = np.transpose(A)

# Stampa la matrice trasposta
print("Trasposta di A:")
print(A_trasposta)
