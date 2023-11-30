import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Funzione che restituisce il sistema di equazioni differenziali del pendolo semplice
def pendulum_system(y, t, g, L):
    theta, omega = y
    dydt = [omega, -g/L * np.sin(theta)]
    return dydt

# Parametri del pendolo
g = 9.81  # accelerazione dovuta alla gravità (m/s^2)
L = 1.0   # lunghezza del pendolo (m)

# Condizioni iniziali
theta0 = np.radians(45)  # angolo iniziale in radianti
omega0 = 0.0             # velocità angolare iniziale

# Array di tempo
t = np.linspace(0, 10, 1000)  # intervallo di tempo da 0 a 10 secondi

# Risolve il sistema di equazioni differenziali
sol = odeint(pendulum_system, [theta0, omega0], t, args=(g, L))

# Estrae l'angolo e la velocità angolare
theta = sol[:, 0]
omega = sol[:, 1]

# Plot dell'angolo rispetto al tempo
plt.figure(figsize=(8, 6))
plt.plot(t, np.degrees(theta), label='Angolo (gradi)')
plt.xlabel('Tempo (s)')
plt.ylabel('Angolo (gradi)')
plt.legend()
plt.grid()
plt.show()

