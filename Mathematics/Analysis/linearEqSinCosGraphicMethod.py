import matplotlib.pyplot as plt
import numpy as np

# Sistema di equazioni lineari
A = np.array([[np.sin(2*np.pi/3), np.cos(2*np.pi/3)], [np.cos(np.pi/4), np.sin(np.pi/4)]])
b = np.array([1, 2])

# Metodo grafico
x = np.linspace(-2, 2, 1000)
y1 = (b[0] - A[0,0]*x) / A[0,1]
y2 = (b[1] - A[1,0]*x) / A[1,1]

# Plot
plt.plot(x, y1, '-r', label='Equazione 1')
plt.plot(x, y2, '-b', label='Equazione 2')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Metodo Grafico')
plt.legend()
plt.show()