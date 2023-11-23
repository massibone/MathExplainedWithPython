import numpy as np
import matplotlib.pyplot as plt

# Coordinate dei punti terminali
terminal_points = np.array([[1, 1], [2, 2], [3, 1], [4, 3]])

# Punto di Steiner (punto aggiuntivo)
steiner_point = np.array([2.5, 1.5])

# Creazione del grafico
plt.figure(figsize=(8, 6))

# Traccia i punti terminali
plt.scatter(terminal_points[:, 0], terminal_points[:, 1], c='red', marker='o', label='Terminal Points')

# Traccia il punto di Steiner
plt.scatter(steiner_point[0], steiner_point[1], c='blue', marker='x', label='Steiner Point')

# Connetti i punti terminali al punto di Steiner
for point in terminal_points:
    plt.plot([point[0], steiner_point[0]], [point[1], steiner_point[1]], 'b--')

# Calcola la lunghezza totale del percorso
total_length = np.sum(np.linalg.norm(terminal_points - steiner_point, axis=1))

plt.xlabel('X')
plt.ylabel('Y')
plt.title(f'Problema di Steiner - Lunghezza Totale: {total_length:.2f}')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
