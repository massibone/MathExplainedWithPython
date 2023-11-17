import matplotlib.pyplot as plt
import numpy as np

# Creazione del cerchio
theta = np.linspace(0, 2*np.pi, 6, endpoint=False)
x = np.cos(theta)
y = np.sin(theta)

# Etichette per i numeri modulo 6
numeri = ['0', '1', '2', '3', '4', '5']

# Creazione del grafico a cerchio
plt.figure(figsize=(6, 6))
plt.plot(x, y, 'o-')

# Aggiungi etichette ai punti
for i, txt in enumerate(numeri):
    plt.annotate(txt, (x[i], y[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Impostazioni del grafico
plt.xlim(-1.2, 1.2)
plt.ylim(-1.2, 1.2)
plt.title('Rappresentazione dei numeri interi modulo 6 su un cerchio')
plt.xlabel('Asse x')
plt.ylabel('Asse y')

# Connetti il primo e l'ultimo punto per chiudere il cerchio
plt.plot([x[0], x[-1]], [y[0], y[-1]], 'o-')

# Mostra il grafico
plt.show()
