'''
Due matrici 
A e B si dicono commutare se il loro prodotto è uguale in entrambi gli ordini, cioè se 

AB=BA.
'''

import numpy as np

# Definizione delle matrici A e B
A = np.array([[1., 0., 0., 0.], [0., 0., 1., 0.], [0., 1., 0., 0.], [0., 0., 0., 1.]])
B = np.array([[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4]])

# Calcolo del prodotto AB e BA
AB = np.dot(A, B)
BA = np.dot(B, A)

# Verifica se le matrici commutano
commute = np.array_equal(AB, BA)

print("Matrice A:")
print(A)

print("\nMatrice B:")
print(B)

print("\nProdotto AB:")
print(AB)

print("\nProdotto BA:")
print(BA)

if commute:
    print("\nLe matrici A e B commutano.")
else:
    print("\nLe matrici A e B non commutano.")

'''
Matrice A:
[[1. 0. 0. 0.]
 [0. 0. 1. 0.]
 [0. 1. 0. 0.]
 [0. 0. 0. 1.]]

Matrice B:
[[1 0 0 0]
 [0 2 0 0]
 [0 0 3 0]
 [0 0 0 4]]

Prodotto AB:
[[1. 0. 0. 0.]
 [0. 0. 3. 0.]
 [0. 2. 0. 0.]
 [0. 0. 0. 4.]]

Prodotto BA:
[[1. 0. 0. 0.]
 [0. 0. 2. 0.]
 [0. 3. 0. 0.]
 [0. 0. 0. 4.]]

Le matrici A e B non commutano.
'''
