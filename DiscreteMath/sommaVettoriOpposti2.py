'''
u =1/2v − w.
'''

import numpy as np
import matplotlib.pyplot as plt

# Definizione dei vettori v e w
v = np.array([3, 2])
w = np.array([1, -1])

# Calcolo di 1/2 * v
half_v = 0.5 * v

# Calcolo del vettore u = 1/2 * v - w
u = half_v - w

# Creazione del grafico
plt.figure()

# Aggiungi vettori al grafico
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='r', label='v')
plt.quiver(0, 0, w[0], w[1], angles='xy', scale_units='xy', scale=1, color='b', label='w')
plt.quiver(0, 0, u[0], u[1], angles='xy', scale_units='xy', scale=1, color='g', label='u (1/2 * v - w)')

# Imposta i limiti del grafico
plt.xlim(-2, 4)
plt.ylim(-2, 3)

# Aggiungi griglia
plt.grid(True)

# Aggiungi etichette degli assi
plt.xlabel('X')
plt.ylabel('Y')

# Aggiungi legenda
plt.legend()

# Mostra il grafico
plt.show()
