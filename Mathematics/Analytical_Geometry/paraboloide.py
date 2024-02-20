import matplotlib.pyplot as plt
import numpy as np

# Definisce la funzione per il paraboloide
def paraboloide(x, y):
  return x**2 + y**2

# Generiamo i dati da graficare
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = paraboloide(X, Y)

# Crea la figura
fig = plt.figure(figsize=(10, 10))
ax = plt.axes(projection='3d')

# Grafica la superficie
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

# Imposta i titoli e le etichette degli assi
ax.set_title('Paraboloide di rotazione')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Mostra la figura
plt.show()
