import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Definizione del sistema di equazioni differenziali
def sistema(t, z):
    x, y = z
    dxdt = y
    dydt = -x
    return [dxdt, dydt]

# Definizione dei tempi in cui campionare la soluzione (metodo di Poincaré)
tempi_poincare = np.arange(0, 20, 0.1)

# Condizioni iniziali
condizioni_iniziali = [1.0, 0.0]

# Risoluzione del sistema di equazioni differenziali usando il metodo di Poincaré
soluzione_poincare = solve_ivp(sistema, [0, 20], condizioni_iniziali, t_eval=tempi_poincare)

# Plot del risultato del metodo di Poincaré
plt.figure(figsize=(8, 4))
plt.plot(soluzione_poincare.y[0], soluzione_poincare.y[1], label='Metodo di Poincaré')
plt.title('Metodo di Poincaré - Sistema di Equazioni Differenziali')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
