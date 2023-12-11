import numpy as np
'''
Cambio x e y valori per verificare che per ogni valore e' simmetrica
Una matrice è definita simmetrica se è uguale alla sua trasposta A = A^t

'''



x=2
y=3
# Definizione delle matrici A e B
A = np.array([[2, x],
              [y**3 - 1, 3 * x**2]])

B = np.array([[1, 5 * (y - x)],
              [5*(y**2 - x**4), 1]])

print("Matrice A:")
print(A)
print("Matrice B:")
print(B)
