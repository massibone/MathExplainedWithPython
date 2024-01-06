'''
dato il sistema di equazione
2x−z=4
y + 2z = 2
2x − y − 3z = 2
'''
import numpy as np

# Definisci la matrice dei coefficienti e il vettore dei termini noti
A = np.array([[2, 0, -1], [0, 1, 2], [2, -1, -3]])
B = np.array([4, 2, 2])

# Risolvi il sistema di equazioni lineari
soluzione = np.linalg.solve(A, B)

# Stampiamo la soluzione
print("La soluzione del sistema è:", soluzione)
#soluzione
# x=2, y=2, z=0
