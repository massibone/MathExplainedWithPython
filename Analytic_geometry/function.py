import numpy as np
import matplotlib.pyplot as plt
# Definisci le funzioni inverse f^-1(y1) e f^-1(y2)


def inv_func1(y1):
    return np.exp(y1)


def inv_func2(y2):
    return np.log(y2)


# Genera alcuni dati di esempio per y1 e y2
y1 = np.linspace(0, 5, 100)
y2 = np.linspace(1, 10, 100)

# Calcola i corrispondenti valori di x1 e x2 utilizzando le funzioni inverse
x1 = inv_func1(y1)
x2 = inv_func2(y2)

# Visualizza i risultati
plt.plot(y1, x1, label='x1 = f^-1(y1)')
plt.plot(y2, x2, label='x2 = f^-1(y2)')
plt.xlabel('y')
plt.ylabel('x')
plt.legend()
plt.show()
