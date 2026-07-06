import matplotlib.pyplot as plt
import numpy as np

# Define the function for the quatrefoil curve
def quatrefoil(t, a):
    return np.cos(2*t)*np.sqrt(np.abs(np.cos(t))) / (np.sin(t)**2 + a**2)

# Define the range of values for t
t = np.linspace(0, 2*np.pi, 1000)

# Set the parameter value for a
a = 1.3

# Calculate the x and y coordinates of the curve
x = quatrefoil(t, a) * np.cos(t)
y = quatrefoil(t, a) * np.sin(t)

# Plot the curve
plt.plot(x, y)

# Set the axis equal and the axis limits
plt.axis('equal')
plt.xlim([-1.5, 1.5])
plt.ylim([-1.5, 1.5])

# Set the axis labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Quatrefoil Curve')

# Show the plot
plt.show()
