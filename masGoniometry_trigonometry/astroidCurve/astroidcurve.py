import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 1000)
a = 1

x = a * np.power(np.cos(t), 3)
y = a * np.power(np.sin(t), 3)

plt.plot(x, y)
plt.axis('equal')
plt.title('Astroid Curve')
plt.show()
