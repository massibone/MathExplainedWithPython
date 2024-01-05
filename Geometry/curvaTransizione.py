

import matplotlib.pyplot as plt
import numpy as np

# Definisci i punti iniziali e finali della transizione
x_start = 0
x_end = 10
y_start = 0
y_end = 5

# Numero di punti per la curva di transizione
num_points = 100

# Calcola i punti della curva di transizione
x_transition = np.linspace(x_start, x_end, num_points)
y_transition = np.linspace(y_start, y_end, num_points)

# Aggiungi una componente di curvatura
y_transition = y_transition + 0.2 * (x_transition - x_start) ** 2

# Crea un grafico per visualizzare la curva di transizione
plt.figure(figsize=(8, 4))
plt.plot(x_transition, y_transition, label='Curva di transizione', color='blue')
plt.plot([x_start, x_end], [y_start, y_end], linestyle='--', color='red', label='Retta originale')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Esempio di Curva di Transizione')
plt.legend()
plt.grid(True)
plt.show()
