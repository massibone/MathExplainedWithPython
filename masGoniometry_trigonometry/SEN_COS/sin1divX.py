import numpy as np
import matplotlib.pyplot as plt

# Definizione del dominio (evitiamo x=0 per evitare divisione per zero)
x = np.linspace(0.001, 1, 1000)

# Calcolo dei valori della funzione sin(1/x)
y = np.sin(1 / x)

# Creazione del grafico
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$\sin(1/x)$')

# Aggiunta di etichette e titolo
plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafico di sin(1/x)')
plt.legend()

# Mostra il grafico
plt.show()
