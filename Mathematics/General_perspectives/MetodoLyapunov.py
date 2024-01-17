import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the Lyapunov system of differential equations
def lyapunov_system(z, t, epsilon):
    x, y = z
    dxdt = y
    dydt = -x - epsilon * x**3
    return [dxdt, dydt]

# Parameter epsilon
epsilon = 0.1

# Initial conditions
initial_conditions_lyapunov = [1.0, 0.0]

# Time points for integration
time_points_lyapunov = np.linspace(0, 20, 500)

# Solve the Lyapunov system of differential equations using odeint
solution_lyapunov = odeint(lyapunov_system, initial_conditions_lyapunov, time_points_lyapunov, args=(epsilon,))

# Plot the result of the Lyapunov method
plt.figure(figsize=(8, 4))
plt.plot(time_points_lyapunov, solution_lyapunov[:, 0], label='Lyapunov Method')
plt.title('Lyapunov Method - System of Differential Equations')
plt.xlabel('Time')
plt.ylabel('x')
plt.legend()
plt.grid(True)
plt.show()
