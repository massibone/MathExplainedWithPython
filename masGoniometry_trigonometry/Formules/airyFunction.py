import numpy as np
import matplotlib.pyplot as plt
from scipy.special import airy

# Define the parameters
x = np.linspace(-10, 10, 1000)

# Calculate the Airy functions Ai(x) and Bi(x)
Aix, Bix, _, _ = airy(x)

# Plot the functions
plt.plot(x, Aix, label='Ai(x)')
plt.plot(x, Bix, label='Bi(x)')
plt.legend()
plt.title('Airy Functions')
plt.xlabel('x')
plt.ylabel('y')
plt.show()