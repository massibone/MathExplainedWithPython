import math
import matplotlib.pyplot as plt
import numpy as np

# Define the angle in radians
angle = np.arange(-2*np.pi, 2*np.pi, 0.1)

# Compute the sine, cosine, and tangent of the angle
sine = np.sinh(angle)
cosine = np.cosh(angle)
tangent = np.tanh(angle)

# Plot the sine, cosine, and tangent curves
plt.ylim(-3,3)
plt.plot(angle, sine, label='Sine')
plt.plot(angle, cosine, label='Cosine')
plt.plot(angle, tangent, label='Tangent')

# Add axis labels and a legend
plt.xlabel('Angle (radians)')
plt.ylabel('Value')
plt.legend()

# Show the plot
plt.show()
