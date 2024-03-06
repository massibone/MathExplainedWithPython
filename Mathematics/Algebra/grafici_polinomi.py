import numpy as np
import matplotlib.pyplot as plt

# Definire le funzioni dei polinomi
def polynomial1(x):
    return x**3 - 3*x + 1

def polynomial2(x):
    return x**4 - x**3 - 4*x**2 + 4*x + 1

# Creare array di valori x
x_values = np.linspace(-3, 3, 400)  # Genera 400 valori equidistanti da -3 a 3

# Calcolare i valori delle funzioni polinomiali per gli array di valori x
y_values1 = polynomial1(x_values)
y_values2 = polynomial2(x_values)

# Creare il grafico
plt.figure(figsize=(10, 6))

# Tracciare il grafico per il primo polinomio
plt.plot(x_values, y_values1, label='x^3 - 3x + 1')

# Tracciare il grafico per il secondo polinomio
plt.plot(x_values, y_values2, label='x^4 - x^3 - 4x^2 + 4x + 1')

# Aggiungere etichette degli assi e una legenda
plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafico dei polinomi')
plt.legend()

# Mostrare il grafico
plt.grid(True)
plt.show()
