import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 2*x - 5  # Definizione della funzione

def lobachevsky(a, b, tol=1e-6, max_iter=100):
    x_old = a
    x_current = b
    for i in range(max_iter):
        x_new = x_current - f(x_current) * (x_current - x_old) / (f(x_current) - f(x_old))
        if abs(x_new - x_current) < tol:
            return x_new, i
        x_old = x_current
        x_current = x_new
    return None, max_iter

# Definizione dell'intervallo
a = 1
b = 3

# Calcolo della soluzione con il metodo di Lobacevskij
root, iterations = lobachevsky(a, b)

# Creazione di un array di valori x per il grafico
x_values = np.linspace(a, b, 100)
y_values = f(x_values)

# Grafico della funzione
plt.plot(x_values, y_values, label='Funzione')

# Grafico del punto di intersezione con l'asse x
plt.scatter(root, 0, color='red', label='Intersezione')

# Etichette degli assi e legenda
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

# Titolo del grafico
plt.title('Grafico della funzione con intersezione')

# Mostra il grafico
plt.show()

# Stampa della soluzione e del numero di iterazioni
print("Metodo di Lobacevskij:")
print("Soluzione:", root)
print("Numero di iterazioni:", iterations)
