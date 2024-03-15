import numpy as np
import matplotlib.pyplot as plt

def radio_decay_law(N0, decay_constant, time):
    """
    Calcola il numero di nuclei radioattivi rimanenti al tempo t
    secondo la legge del decadimento del radio.
    
    Argomenti:
    N0 : float
        Numero iniziale di nuclei radioattivi.
    decay_constant : float
        Costante di decadimento (tasso di decadimento).
    time : array-like
        Array di valori temporali in cui calcolare il numero di nuclei.
    
    Ritorna:
    array-like
        Numero di nuclei radioattivi rimanenti al tempo t.
    """
    return N0 * np.exp(-decay_constant * time)

# Parametri del problema
N0 = 1000  # Numero iniziale di nuclei radioattivi
decay_constant = 0.05  # Costante di decadimento (tasso di decadimento)

# Tempo di osservazione
time = np.linspace(0, 10, 100)  # Tempo da 0 a 10 unità di tempo

# Calcola il numero di nuclei radioattivi rimanenti al tempo t
radioactive_nuclei = radio_decay_law(N0, decay_constant, time)

# Plot del numero di nuclei radioattivi in funzione del tempo
plt.plot(time, radioactive_nuclei, label='Numero di nuclei radioattivi')
plt.xlabel('Tempo')
plt.ylabel('Numero di nuclei radioattivi')
plt.title('Decadimento radioattivo secondo la legge del decadimento del radio')
plt.legend()
plt.grid(True)
plt.show()

