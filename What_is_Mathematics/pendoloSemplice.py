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
