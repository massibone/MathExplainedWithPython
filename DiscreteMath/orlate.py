
'''
Per calcolare l'orlata della matrice A 
rispetto al vettore (2, 3, 1, 3), 
possiamo moltiplicare il vettore 
per ogni riga di A
'''
import numpy as np

# Definisci la matrice A
A = np.array([[3, 1, 2],
              [0, 1, 4],
              [3, 3, -2],
              [5, 0, 0],
              [1, 1, -1]])

# Definisci rispetto al vettore
vettore = np.array([2, 3, 1, 3])

# Calcola l'orlata di A rispetto al vettore
orlata = A @ vettore

print(orlata)
