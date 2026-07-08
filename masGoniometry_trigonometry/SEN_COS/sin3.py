import numpy as np
import matplotlib.pyplot as plt

# Definizione della funzione f(x) = (sin x)^2
def f1(x):
    return np.sin(x)**2

# Definizione della funzione f(x) = |sin x|
def f2(x):
    return np.abs(np.sin(x))

# Definizione del dominio x
x = np.linspace(0, 2*np.pi, 100)

# Calcolo dei valori delle funzioni
y1 = f1(x)
y2 = f2(x)

# Tracciamento delle funzioni
plt.plot(x, y1, label='(sin x)^2')
plt.plot(x, y2, label='|sin x|')

# Configurazione del grafico
plt.title("Funzioni (sin x)^2 e |sin x|")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

# Mostra il grafico
plt.show()
