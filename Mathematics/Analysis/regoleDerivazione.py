import numpy as np
import matplotlib.pyplot as plt

# Definisci la variabile indipendente x
x = np.linspace(-5, 5, 400)

# Definisci le funzioni
def somma(x):
    return x**2 + np.sin(x)

def moltiplicazione(x):
    return x * np.cos(x)

def quoziente(x):
    return np.sin(x) / (x + 1)

def inversa(x):
    return 1 / x

# Calcola le derivate
der_somma = np.gradient(somma(x), x)
der_moltiplicazione = np.gradient(moltiplicazione(x), x)
der_quoziente = np.gradient(quoziente(x), x)
der_inversa = np.gradient(inversa(x), x)

# Plotta le funzioni e le loro derivate
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(x, somma(x), label='f(x) = x^2 + sin(x)')
plt.plot(x, der_somma, label="f'(x)")
plt.title('Derivata di una somma')
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(x, moltiplicazione(x), label='f(x) = x * cos(x)')
plt.plot(x, der_moltiplicazione, label="f'(x)")
plt.title('Derivata di una moltiplicazione')
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(x, quoziente(x), label='f(x) = sin(x) / (x + 1)')
plt.plot(x, der_quoziente, label="f'(x)")
plt.title('Derivata di un quoziente')
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(x, inversa(x), label='f(x) = 1 / x')
plt.plot(x, der_inversa, label="f'(x)")
plt.title('Derivata di una funzione inversa')
plt.legend()

plt.tight_layout()
plt.show()
