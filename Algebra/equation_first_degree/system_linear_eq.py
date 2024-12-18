import numpy as np
import matplotlib.pyplot as plt

# definizione delle equazioni delle rette
x = np.linspace(-5, 5, 100)
y1 = (7 - 6*x) / 3
y2 = (3*x + 2) / 2

# creazione del grafico
plt.plot(x, y1, label='6x + 3y = 7')
plt.plot(x, y2, label='3x - 2y = -2')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()

# visualizzazione del grafico
plt.show()
