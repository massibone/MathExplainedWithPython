import numpy as np

# Definisci la matrice dei coefficienti A
A = np.array([[2, 1, 3],
              [1, 0.5, 6],
              [1, 0.5, 3]])

# Definisci la matrice completa estesa B
B = np.array([[2, 1, 3, 1],
              [1, 0.5, 6, 2],
              [1, 0.5, 3, 1]])

# Calcola il rango di A e B
rank_A = np.linalg.matrix_rank(A)
rank_B = np.linalg.matrix_rank(B)

# Controlla se le equazioni sono linearmente indipendenti
if rank_A == A.shape[1]:
    print("Le equazioni sono linearmente indipendenti.")
else:
    print("Le equazioni non sono linearmente indipendenti.")

# Verifica la compatibilità del sistema
if rank_A == rank_B and rank_A == A.shape[1]:
    print("Il sistema è compatibile ed ha una soluzione.")
elif rank_A == rank_B and rank_A < A.shape[1]:
    print("Il sistema ha infinitamente molte soluzioni.")
else:
    print("Il sistema è incompatibile e non ha soluzioni.")
