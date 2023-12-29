'''
Date due matrici 2x2 con valori x, y, coseno, seno, x^4 e x^2 
come faccio a creare la matrice C = α * (AB + BA) - βI2 
(Beta * matrice Identità)
'''

import numpy as np

# Definizione dei valori x, y e altre costanti
x = 1.0  # Esempio: x = 1.0
y = 2.0  # Esempio: y = 2.0
alpha = 2.0
beta = 3.0

# Creazione delle matrici A e B
A = np.array([[x, y], [np.cos(x), np.sin(x)]])
B = np.array([[x**4, x**2], [y, np.cos(x)]])

# Calcolo di AB e BA
AB = np.dot(A, B)
BA = np.dot(B, A)

# Calcolo di alpha * (AB + BA)
alpha_times_AB_plus_BA = alpha * (AB + BA)

# Calcolo di beta * I2
beta_times_I2 = beta * np.eye(2)

# Calcolo della matrice C
C = alpha_times_AB_plus_BA - beta_times_I2

# Stampa della matrice C
print("Matrice C:\n", C)
