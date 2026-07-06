#The torpedo curve, also known as Viviani's curve, is a space curve formed by the intersection of a torus and a cylinder.

import matplotlib.pyplot as plt
import numpy as np

# Define the function for the torpedo curve
def strophoid(theta, a):
    return a * np.tan(theta) / (1 - np.tan(theta)**2)

# Define the range of values for theta
theta = np.linspace(-np.pi/2 + 0.01, np.pi/2 - 0.01, 1000)

# Set the parameter value for a
a = 1

# Calculate the x and y coordinates of the curve
x = strophoid(theta, a) * np.cos(theta)
y = strophoid(theta, a) * np.sin(theta)

# Plot the curve
plt.plot(x, y)

# Set the x and y axis limits
plt.xlim([-2, 2])
plt.ylim([-2, 2])

# Set the axis labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Torpedo Curve')

# Show the plot
plt.show()

