import numpy as np
import matplotlib.pyplot as plt# Define fixed line
x = np.linspace(-5, 5, 100)
y = x
# Define distance constant
d = 2
# Define TN constant curve
t = np.linspace(-5, 5, 100)
x_tn = t - np.sqrt(d**2 - 1) * np.sin(np.arctan(t))
y_tn = t + np.sqrt(d**2 - 1) * np.cos(np.arctan(t))

# Plot TN constant curve and fixed line
plt.plot(x_tn, y_tn, label='TN constant curve')
plt.plot(x, y, '--', label='Fixed line')
plt.axis('equal')
plt.legend()
plt.title('TN constant curve')
plt.show()

