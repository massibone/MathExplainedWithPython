'''
dato il sistema
2x1 − x2 + 6x4 = 2
x1 + 2x2 − x3 + 2x4 = 1
x2 − 2x3 + x4 = 1

come si trovano le soluzioni? 

'''
import numpy as np

# Definisci la matrice dei coefficienti e il vettore dei termini noti
A = np.array([[2, -1, 0, 6], [1, 2, -1, 2], [0, 1, -2, 1]])
B = np.array([2, 1, 1])

# Risolvi il sistema di equazioni lineari
soluzione = np.linalg.solve(A, B)

# Stampa la soluzione
print("La soluzione del sistema è:", soluzione)


