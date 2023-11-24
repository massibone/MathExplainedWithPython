'''
Si consideri l’applicazione lineare f : M(3; R) → M(4; R) tale che
f (0; 1; 1) = (3; 2; 0; 1)
f (1; 0; 1) = (1; −1; 1; 0)
f (2; 0; 0) = (0; 0; 2; 0):
Allora la matrice A ∈ M(4; 3; R) tale che f = fA associata alla base ((0; 1; 1);(1; 0; 1);(2; 0; 0)) è:

La matrice A associata alla base ((0; 1; 1);(1; 0; 1);(2; 0; 0)) è data dalle colonne che sono le immagini dei vettori di base. Quindi, la matrice A è:
A=​3201​1−110​0020​​
Ogni colonna di A è l’immagine del corrispondente vettore di base sotto l’applicazione lineare f. Ad esempio, la prima colonna è f(0; 1; 1), la seconda colonna è f(1; 0; 1), e la terza colonna è f(2; 0; 0).
'''
import numpy as np

# Definisci le immagini dei vettori di base
v1 = np.array([3, 2, 0, 1])
v2 = np.array([1, -1, 1, 0])
v3 = np.array([0, 0, 2, 0])

# Crea la matrice A
A = np.column_stack((v1, v2, v3))

print(A)

