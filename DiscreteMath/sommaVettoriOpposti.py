import numpy as np
import matplotlib.pyplot as plt

# Definizione dei vettori v e w
v = np.array([3, 2])
w = np.array([1, -1])

# Calcolo dell'opposto di v e w
opposite_v = -v
opposite_w = -w

# Calcolo del vettore a = -v - w
a = opposite_v + opposite_w

# Creazione del grafico
plt.figure()

# Aggiungi vettori al grafico
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='r', label='v')
plt.quiver(0, 0, w[0], w[1], angles='xy', scale_units='xy', scale=1, color='b', label='w')
plt.quiver(0, 0, a[0], a[1], angles='xy', scale_units='xy', scale=1, color='g', label='a (−v - w)')

# Imposta i limiti del grafico
plt.xlim(-4, 4)
plt.ylim(-4, 4)

# Aggiungi griglia
plt.grid(True)

# Aggiungi etichette degli assi
plt.xlabel('X')
plt.ylabel('Y')

# Aggiungi legenda
plt.legend()

# Mostra il grafico
plt.show()
