'''
Si consideri l’applicazione lineare f : M(3; R) → M(4; R) tale che
f (0; 1; 1) = (3; 2; 0; 1)
f (1; 0; 1) = (1; −1; 1; 0)
f (2; 0; 0) = (0; 0; 2; 0):
Allora la matrice A ∈ M(4; 3; R) associata alla base canonica tale che f = fA è
0 2 1
0 3 −1
1 0 0
0 1 0
'''
import numpy as np

# Definire i vettori immagine f(e_i)
f_e1 = np.array([0, 2, 1, 0])
f_e2 = np.array([0, 3, -1, 1])
f_e3 = np.array([1, 0, 0, 0])

# Organizzare i vettori come colonne della matrice A
A = np.column_stack((f_e1, f_e2, f_e3))

print("La matrice A è:")
print(A)
