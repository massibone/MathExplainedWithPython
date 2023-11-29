import numpy as np
import matplotlib.pyplot as plt

# Calcola le radici z_k
n_vertices = 7
angles = np.linspace(0, 2 * np.pi, n_vertices, endpoint=False)
z_k = np.exp(1j * angles)

# Estrarre le coordinate x e y dei vertici
x_vertices = np.real(z_k)
y_vertices = np.imag(z_k)

# Aggiungi il primo vertice all'inizio per chiudere il poligono
x_vertices = np.append(x_vertices, x_vertices[0])
y_vertices = np.append(y_vertices, y_vertices[0])

# Visualizza il poligono (ettagono)
plt.plot(x_vertices, y_vertices, 'b-')
plt.scatter(x_vertices, y_vertices, color='red')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.xlabel('Parte reale')
plt.ylabel('Parte immaginaria')
plt.title('Ettagono regolare inscritto')
plt.axis('equal')
plt.show()
