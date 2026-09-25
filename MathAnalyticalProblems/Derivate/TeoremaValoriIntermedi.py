
'''
se una funzione è continua in un intervallo chiuso e limitato di ℝ, 
allora la funzione assume ogni valore tra il valore minimo
e il valore massimo della funzione in quell'intervallo. 
'''
import numpy as np
import matplotlib.pyplot as plt

# Definizione di una funzione continua su un intervallo
def funzione(x):
    return x**3 - 3*x**2 + 2

# Intervallo chiuso e limitato
intervallo_inizio = -1
intervallo_fine = 3
# Calcolare il valore minimo e massimo della funzione nell'intervallo
valore_minimo = min([funzione(x) for x in np.linspace(intervallo_inizio, intervallo_fine, 1000)])
valore_massimo = max([funzione(x) for x in np.linspace(intervallo_inizio, intervallo_fine, 1000)])

# Calcolare i valori intermedi tra il minimo e il massimo
valori_intermedi = np.linspace(valore_minimo, valore_massimo, 100)

# Plot della funzione
x = np.linspace(intervallo_inizio, intervallo_fine, 1000)
y = funzione(x)
plt.plot(x, y, label='f(x) = x^3 - 3x^2 + 2')

# Plot dei valori intermedi
plt.scatter([intervallo_inizio] * 100, valori_intermedi, c='red', marker='.')
plt.scatter([intervallo_fine] * 100, valori_intermedi, c='red', marker='.')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Teorema dei Valori Intermedi')
plt.legend()
plt.grid(True)

plt.show()
