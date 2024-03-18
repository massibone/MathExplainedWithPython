'''
Questo codice utilizza il modulo scipy.integrate.solve_ivp per risolvere numericamente il sistema di equazioni differenziali che descrivono il movimento del pendolo matematico
'''
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Definizione delle costanti
g = 9.81  # Accelerazione di gravità in m/s^2
l = 1.0   # Lunghezza del pendolo in metri

# Definizione della funzione per il sistema di equazioni differenziali
def pendolo(t, y):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = -(g / l) * np.sin(theta)
    return [dtheta_dt, domega_dt]

# Condizioni iniziali
theta_0 = np.pi / 4  # Angolo iniziale in radianti
omega_0 = 0.0        # Velocità angolare iniziale in rad/s
y0 = [theta_0, omega_0]

# Intervallo di tempo
t_span = (0, 10)  # Intervallo di tempo da 0 a 10 secondi

# Risoluzione del sistema di equazioni differenziali
sol = solve_ivp(pendolo, t_span, y0, t_eval=np.linspace(0, 10, 1000))

# Plot del risultato
plt.figure(figsize=(8, 6))
plt.plot(sol.t, sol.y[0], 'b', label='Angolo (theta)')
plt.xlabel('Tempo (s)')
plt.ylabel('Angolo (rad)')
plt.title('Movimento del pendolo matematico')
plt.legend()
plt.grid(True)
plt.show()
