'''
Direzione di un vettore: La direzione di un vettore è la linea o il percorso che segue. Due vettori hanno la stessa direzione se sono paralleli.

Verso di un vettore: Il verso di un vettore è la direzione in cui il vettore "punta". Due vettori hanno lo stesso verso se si muovono nella stessa direzione.

Equipollenza di vettori: Due vettori sono equipollenti se hanno la stessa direzione, lo stesso verso e la stessa lunghezza.
'''

import numpy as np
import matplotlib.pyplot as plt

# Definizione dei vettori P, Q, Q' e P'
P = np.array([0, 0])   # Punto di origine
Q = np.array([3, 2])   # Coordinata finale per Q
Q_prime = np.array([1, 4])  # Coordinata finale per Q'
P_prime = np.array([4, 3])  # Coordinata finale per P'

# Creazione del grafico
plt.figure()

# Aggiungi vettori al grafico
plt.quiver(*P, *Q, color='b', scale=1, scale_units='xy', angles='xy')
plt.quiver(*P, *P_prime, color='r', scale=1, scale_units='xy', angles='xy')
plt.quiver(*Q_prime, *(P_prime - Q_prime), color='g', scale=1, scale_units='xy', angles='xy')

# Imposta i limiti del grafico
plt.xlim(-1, 5)
plt.ylim(-1, 5)

# Aggiungi griglia
plt.grid(True)

# Etichette degli assi
plt.xlabel('X')
plt.ylabel('Y')

# Mostra il grafico
plt.show()
