
import numpy as np
import matplotlib.pyplot as plt

# Dati delle flussioni
posizioni = np.array([0.0, 1.0, 2.0, 3.0, 4.0]) # Posizioni in metri
tempi = np.array([0.0, 0.5, 1.0, 1.5, 2.0]) # Tempi in secondi

# Calcola la velocità istantanea
velocità = np.gradient(posizioni, tempi)

# Plot del grafico
plt.plot(tempi, velocità)
plt.xlabel('Tempo (s)')
plt.ylabel('Velocità (m/s)')
plt.show()
'''
I dati delle flussioni sono le posizioni in metri e i tempi in secondi. 
Il metodo delle flussioni calcola la velocità istantanea come la derivata 
delle posizioni rispetto ai tempi. 
Questo viene fatto utilizzando la funzione `numpy.gradient`. 

'''
