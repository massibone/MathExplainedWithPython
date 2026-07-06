import math
import matplotlib.pyplot as plt
import numpy as np

# Genera un array di valori in radianti
x_radiani = np.linspace(-math.pi/2, math.pi/2, 100)

# Calcola l'equivalente in gradi di ogni valore in x_radiani
x_gradi = np.array([math.degrees(xi) for xi in x_radiani])

# Crea un grafico con i valori di x_gradi sull'asse x e i valori di x_radiani sull'asse y
plt.plot(x_gradi, x_radiani)

# Aggiunge una griglia al grafico
plt.grid(True)

# Aggiunge etichette agli assi
plt.xlabel('Valori di x (gradi)')
plt.ylabel('Valori di x (radianti)')

# Mostra il grafico
plt.show()
