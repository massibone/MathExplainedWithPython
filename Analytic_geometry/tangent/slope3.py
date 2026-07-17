import numpy as np
import matplotlib.pyplot as plt

# Define the circle's center and radius
a, b = 3, 5 # center coordinates
r = 5 # radius

# Define the slope of the tangent lines
m = -3/4

# Calculate the y-intercepts of the tangent lines
c1 = b + r / np.sqrt(1 + m**2)
c2 = b - r / np.sqrt(1 + m**2)

# Generate x and y data points for the circle
theta = np.linspace(0, 2*np.pi, 100)
x = a + r * np.cos(theta)
y = b + r * np.sin(theta)

# Generate x data points for the tangent lines
x_t = np.linspace(a-r-1, a+r+1, 100)
Y_t = np.linspace(a-r-1,a+r,100)
# Calculate y data points for the tangent lines
y_t1 = m * x_t + c1 +5
y_t2 = m * x_t + c2

# Plot the circle and tangent lines
fig, ax = plt.subplots()
ax.plot(x, y, color='black', label='Circle')
ax.plot(Y_t, y_t1, color='red', linestyle='--', label='Tangent line 1')
ax.plot(x_t, y_t2, color='blue', linestyle='--', label='Tangent line 2')

# Add a legend and axis labels
ax.legend()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Tangent Lines to a Circle')

# Display the plot
plt.show()
