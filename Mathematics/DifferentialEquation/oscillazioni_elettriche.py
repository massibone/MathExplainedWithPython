'''
simula le oscillazioni elettriche in un semplice circuito oscillante, rappresentato dal circuito LC (induttanza-capacità) con una resistenza in serie
'''
import numpy as np
import matplotlib.pyplot as plt

# Definizione delle costanti del circuito
C = 1.0  # Capacità del condensatore in farad (F)
L = 1.0  # Induttanza dell'induttore in henry (H)
R = 0.1  # Resistenza in ohm (Ω)

# Definizione delle condizioni iniziali
q0 = 1.0  # Carica iniziale sul condensatore in coulomb (C)
i0 = 0.0  # Corrente iniziale attraverso l'induttore in ampere (A)

# Definizione della funzione delle derivate
def circuito(t, y):
    q, i = y
    dq_dt = i / C
    di_dt = (-1 / L) * (q / C) - (R / L) * i
    return [dq_dt, di_dt]

# Tempo di simulazione
t_start = 0.0
t_stop = 10.0
num_punti = 1000
t = np.linspace(t_start, t_stop, num_punti)

# Risoluzione del sistema di equazioni differenziali
from scipy.integrate import solve_ivp
sol = solve_ivp(circuito, [t_start, t_stop], [q0, i0], t_eval=t)

# Plot delle soluzioni
plt.figure(figsize=(10, 6))
plt.plot(sol.t, sol.y[0], 'b', label='Carica sul condensatore (C)')
plt.plot(sol.t, sol.y[1], 'r', label='Corrente attraverso l\'induttore (A)')
plt.xlabel('Tempo (s)')
plt.ylabel('Carica (C) / Corrente (A)')
plt.title('Oscillazioni elettriche nel circuito LC con resistenza')
plt.legend()
plt.grid(True)
plt.show()
