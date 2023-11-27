'''
Il teorema di Liouville è un risultato fondamentale in meccanica statistica, 
che riguarda la conservazione della fase nello spazio delle fasi di un sistema dinamico hamiltoniano.
Un sistema dinamico hamiltoniano è un sistema dinamico in cui 
l'evoluzione temporale del sistema è determinata da un'equazione differenziale di Hamilton.
L'equazione differenziale di Hamilton per il pianeta è la seguente:

dH/dt = 0
Questa equazione significa che l'Hamiltoniana è una funzione costante del tempo. In altre parole, l'energia totale del sistema è conservata.
'''
import numpy as np
import matplotlib.pyplot as plt

# Genera una distribuzione casuale di particelle nello spazio delle fasi
np.random.seed(0)
num_particles = 1000
q = np.random.rand(num_particles)  # coordinate q casuali
p = np.random.rand(num_particles)  # impulsi p casuali

# Plot della distribuzione nello spazio delle fasi
plt.figure(figsize=(8, 6))
plt.scatter(q, p, alpha=0.5)
plt.xlabel('Coordinate q')
plt.ylabel('Impulsi p')
plt.title('Distribuzione casuale nello spazio delle fasi')
plt.grid()
plt.show()
