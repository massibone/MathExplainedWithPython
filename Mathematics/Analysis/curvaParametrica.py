import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Definizione delle variabili simboliche
t = sp.symbols('t')

# Definizione delle coordinate della curva parametrica
x = t**2
y = t**3

# Calcolo delle derivate prima e seconda rispetto a t
dx_dt = sp.diff(x, t)
dy_dt = sp.diff(y, t)
d2x_dt2 = sp.diff(dx_dt, t)
d2y_dt2 = sp.diff(dy_dt, t)

# Calcolo del raggio del cerchio avente la stessa curvatura
curvatura_cerchio = 1 / sp.symbols('R')
r = sp.sqrt(dx_dt**2 + dy_dt**2)
cross_product = dx_dt * d2y_dt2 - dy_dt * d2x_dt2
raggio_cerchio = sp.simplify(sp.Abs(cross_product) / (curvatura_cerchio * d2x_dt2**2))

# Creazione di funzioni numeriche per la curva e il cerchio
funzione_curva = sp.lambdify(t, (x, y), 'numpy')
funzione_cerchio = sp.lambdify(t, (x + raggio_cerchio * np.cos(np.arctan2(dy_dt, dx_dt)), 
                                  y + raggio_cerchio * np.sin(np.arctan2(dy_dt, dx_dt))), 'numpy')

# Creazione di valori numerici per t
valori_t = np.linspace(-2, 2, 100)

# Calcolo delle coordinate della curva e del cerchio
curve_coords = funzione_curva(valori_t)
cerchio_coords = funzione_cerchio(valori_t)

# Plot della curva e del cerchio
plt.figure(figsize=(8, 8))
plt.plot(curve_coords[0], curve_coords[1], label='Curva parametrica')
plt.plot(cerchio_coords[0], cerchio_coords[1], label='Cerchio con la stessa curvatura', linestyle='--')
plt.title('Curva parametrica e Cerchio con la stessa curvatura')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()
