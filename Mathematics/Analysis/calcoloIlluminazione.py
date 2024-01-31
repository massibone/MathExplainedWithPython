'''
si consideri un pilastroe eretto al centro di una pista da pattinaggio circolare e 
sormontato da una lampada ad altezza h. 
L'illuminazione T sul bordo de cerchio è: T= A sin alfa/(h^2+r^2) 
'''

import matplotlib.pyplot as plt
import numpy as np

def calcola_illuminazione(A, alpha, h, r):
    # Calcola l'illuminazione T sulla circonferenza del cerchio
    angolo_radiani = np.radians(alpha)
    T = A * np.sin(angolo_radiani) / (h**2 + r**2)
    return T

# Parametri
A = 1.0  # Costante
alpha = 30.0  # Angolo in gradi
h = 3.0  # Altezza della lampada sopra il suolo
r = 5.0  # Raggio del cerchio (pista da pattinaggio)

# Calcola l'illuminazione utilizzando la funzione
illuminazione_circonferenza = calcola_illuminazione(A, alpha, h, r)

# Visualizza il cerchio
theta = np.linspace(0, 2*np.pi, 100)
x = r * np.cos(theta)
y = r * np.sin(theta)

plt.figure(figsize=(8, 8))
plt.plot(x, y, label='Circonferenza (Pista da pattinaggio)')
plt.scatter(0, 0, color='red', marker='o', label='Pilastro/Lampada')

plt.title('Pista da Pattinaggio con Pilastro e Lampada')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.axis('equal')

# Stampa l'illuminazione sulla circonferenza
plt.text(0, r + 1, f'Illuminazione sulla circonferenza: {illuminazione_circonferenza:.4f}', ha='center')

# Mostra il grafico
plt.show()
