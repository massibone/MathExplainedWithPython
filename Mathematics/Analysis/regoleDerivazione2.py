import numpy as np
import matplotlib.pyplot as plt

# Definisci la variabile indipendente x
x = np.linspace(-2, 2, 400)

# Funzione 1: y = cos^3(x^2)
y1 = np.cos(x**2)**3
dy1_dx = -6 * x * np.sin(x**2) * np.cos(x**2)**2

# Funzione 2: y = u^3, dove u = 3x + 4
u = 3*x + 4
y2 = u**3
dy2_dx = 3 * u**2 * 3

# Funzione 3: y = 3x + 4
y3 = 3*x + 4
dy3_dx = 3

# Plotta le funzioni e le loro derivate
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(x, y1, label=r'$\cos^3(x^2)$')
plt.title('Funzione originale')

plt.subplot(2, 2, 2)
plt.plot(x, dy1_dx, label=r"$\frac{dy}{dx}$")
plt.title('Derivata della funzione')

plt.subplot(2, 2, 3)
plt.plot(x, y2, label=r'$u^3$, $u=3x+4$')
plt.title('Funzione originale')

plt.subplot(2, 2, 4)
plt.plot(x, dy2_dx, label=r"$\frac{dy}{dx}$")
plt.title('Derivata della funzione')

plt.tight_layout()
plt.show()

