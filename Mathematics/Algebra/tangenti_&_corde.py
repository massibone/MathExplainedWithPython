import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 2*x - 5  # Definizione della funzione

def df(x):
    return 3*x**2 - 2  # Derivata della funzione

def metodo_delle_tangenti(x0, tol=1e-6, max_iter=100):
    x_old = x0
    for i in range(max_iter):
        x_new = x_old - f(x_old) / df(x_old)
        if abs(x_new - x_old) < tol:
            return x_new, i
        x_old = x_new
    return None, max_iter

def metodo_delle_corde(a, b, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        x_new = (a*f(b) - b*f(a)) / (f(b) - f(a))
        if abs(f(x_new)) < tol:
            return x_new, i
        if f(a) * f(x_new) < 0:
            b = x_new
        else:
            a = x_new
    return None, max_iter

# Definizione dell'intervallo
a = 1
b = 3

# Calcolo delle soluzioni
x_tangenti, iter_tangenti = metodo_delle_tangenti(a)
x_corde, iter_corde = metodo_delle_corde(a, b)

# Creazione di un array di valori x per il grafico
x_values = np.linspace(a, b, 100)
y_values = f(x_values)

# Grafico della funzione
plt.plot(x_values, y_values, label='Funzione')

# Grafico dei punti di intersezione con l'asse x
plt.scatter([x_tangenti, x_corde], [0, 0], color='red', label='Intersezioni')

# Etichette degli assi e legenda
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

# Titolo del grafico
plt.title('Grafico della funzione e intersezioni')

# Mostra il grafico
plt.show()

# Stampa delle soluzioni e del numero di iterazioni
print("Metodo delle tangenti:")
print("Soluzione:", x_tangenti)
print("Numero di iterazioni:", iter_tangenti)

print("\nMetodo delle corde:")
print("Soluzione:", x_corde)
print("Numero di iterazioni:", iter_corde)
