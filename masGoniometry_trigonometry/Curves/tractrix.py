import matplotlib.pyplot as plt
import numpy as np
'''
Other name: equitangential curve 
(because the tangent:T is constant along this curve)



'''

# Define the function for the tractrix curve
def tractrix(t, a):
    return a * np.log(np.abs((t + np.sqrt(t**2 + a**2)) / a))

# Define the range of values for t
t = np.linspace(-10, 10, 1000)

# Set the parameter value for a
a = 1

# Calculate the x and y coordinates of the curve
x = a * np.log(np.abs((t + np.sqrt(t**2 + a**2)) / a)) - t
y = a * np.sqrt(np.abs(t**2 + a**2) - a**2)

# Plot the curve
plt.plot(x, y)

# Set the x and y axis limits
plt.xlim([-5, 5])
plt.ylim([0, 5])

# Set the axis labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Tractrix Curve')

# Show the plot
plt.show()
