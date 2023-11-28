import numpy as np

# Definizione delle matrici A e B
A = np.array([[1, 0, 2], [0, 0, 2], [3, 1, 0], [1, 5, 0]])
B = np.array([[1, 1, 0], [1, 0, 3], [0, 1, 2], [2, 7, 1]])

# Calcolo della matrice X
X = B - A.T

print("Matrice X:")
print(X)

'''
A + X^t = B
semplificato
X^t = B - A
'''