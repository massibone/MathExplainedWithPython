'''
programma Python per calcolare il potenziale 
di un campo elettrico generato da un sistema arbitrario di cariche, 
basato sulla legge di Coulomb
'''
import numpy as np

# Costante elettrica Coulombiana (N m^2/C^2)
k = 8.9875e9  

# Funzione per calcolare il potenziale generato da una carica puntiforme
def potenziale_carica(q, posizione_carica, posizione_osservatore):
    distanza = np.linalg.norm(posizione_osservatore - posizione_carica)
    return k * q / distanza

# Funzione per calcolare il potenziale generato da un sistema di cariche
def potenziale_sistema(cariche, posizioni_cariche, posizione_osservatore):
    potenziale_totale = 0
    for i in range(len(cariche)):
        potenziale_totale += potenziale_carica(cariche[i], posizioni_cariche[i], posizione_osservatore)
    return potenziale_totale

# Esempio di sistema di cariche
cariche = np.array([1e-6, -2e-6, 3e-6])  # Cariche in Coulomb
posizioni_cariche = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -1]])  # Posizioni delle cariche

# Posizione dell'osservatore
posizione_osservatore = np.array([0, 0, 0])

# Calcolo del potenziale
potenziale = potenziale_sistema(cariche, posizioni_cariche, posizione_osservatore)

# Stampare il risultato
print(f"Il potenziale nel punto {posizione_osservatore} è: {potenziale:.2f} Volt")
