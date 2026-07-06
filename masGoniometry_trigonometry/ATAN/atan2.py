


import math
import matplotlib.pyplot as plt
import numpy as np

# Genera un array di valori in radianti
x = np.linspace(-math.pi/2, math.pi/2, 100)

# Calcola l'arco tangente di ogni valore in x
y = np.array([math.atan(xi) for xi in x])

# Crea un grafico con i valori di x sull'asse x e i valori di y sull'asse y
plt.plot(x, y)

# Aggiunge una griglia al grafico
plt.grid(True)

# Aggiunge etichette agli assi
plt.xlabel('Valori di x (radianti)')
plt.ylabel('Arco tangente di x')

# Mostra il grafico
plt.show()
