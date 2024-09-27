'''
La decomposizione LU scompone una matrice 
A in una matrice triangolare inferiore 
L e una matrice triangolare superiore U. 
'''
import numpy as np
import scipy.linalg

# Creiamo una matrice esempio
A = np.array([[4, 3], [6, 3]])

# Decomposizione LU
P, L, U = scipy.linalg.lu(A)

print("Matrice originale A:")
print(A)
print("Matrice di permutazione P:")
print(P)
print("Matrice triangolare inferiore L:")
print(L)
print("Matrice triangolare superiore U:")
print(U)
-decomposizioneQR.py
# Decomposizione QR
Q, R = np.linalg.qr(A)

print("Matrice ortogonale Q:")
print(Q)
print("Matrice triangolare superiore R:")
print(R)

