#the ellipse and the toroid, with the toroid having the same diameter as the ellipse and having constant width.

import numpy as np
import matplotlib.pyplot as plt

# Define ellipse parameters
a = 2
b = 1

# Define toroid parameters
d = 2*a
R = (d - 2*b)/2
a_t = a - R

# Define ellipse equation
t = np.linspace(0, 2*np.pi, 100)
x_e = a * np.cos(t)
y_e = b * np.sin(t)

# Define toroid equation
theta = np.linspace(0, 2*np.pi, 100)
x_t = (a_t + R * np.cos(theta)) * np.cos(t)
y_t = (a_t + R * np.cos(theta)) * np.sin(t) + R * np.sin(theta)

# Plot ellipse and toroid
plt.plot(x_e, y_e, 'b', label='Ellipse')
plt.plot(x_t, y_t, 'g', label='Toroid')
plt.axis('equal')
plt.legend()
plt.title('Constant Width Curve')
plt.show()
