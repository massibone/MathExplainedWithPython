
'''
Per determinare se tutte le orlati di A rispetto al vettore (1, 3, 4, 2, 3, 4) hanno determinante nullo, è necessario calcolare il determinante di ciascuna orlata. 
'''

import numpy as np

# Definisci la matrice A
A = np.array([[4, 1, 3, 0],
              [-2, 3, -5, 0],
              [0, 2, -2, 3],
              [1, -1, 2, 0]])

# Definisci il vettore
vettore = np.array([1, 3, 4, 2, 3, 4])

# Inizializza una lista per memorizzare i determinanti
determinanti = []

# Calcola il determinante di ogni orlata
for i in range(A.shape[1]):
    orlata = np.delete(A, i, axis=1)  # Rimuovi la colonna i-esima
    orlata[:, i] = vettore  # Sostituisci la colonna i-esima con il vettore
    determinante = np.linalg.det(orlata)  # Calcola il determinante dell'orlata
    determinanti.append(determinante)

# Verifica se tutti i determinanti sono nulli
if all(d == 0 for d in determinanti):
    print("Tutte le orlati hanno determinante nullo.")
else:
    print("Almeno una delle orlati ha un determinante non nullo.")
