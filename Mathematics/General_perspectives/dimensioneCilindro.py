'''
er trovare le dimensioni del recipiente cilindrico che ha superficie minima a parità di volume, 
possiamo formulare il problema come un problema di ottimizzazione. 
'''

from scipy.optimize import minimize_scalar
import numpy as np

# Funzione da minimizzare: superficie totale del cilindro
def funzione_superficie(raggio):
    altezza = 2 * raggio  # Altezza uguale al diametro di base
    superficie_laterale = 2 * np.pi * raggio * altezza
    superficie_fondo = np.pi * raggio**2
    superficie_totale = superficie_laterale + superficie_fondo
    return superficie_totale

# Trova il minimo della funzione (superficie minima)
risultato = minimize_scalar(funzione_superficie, bounds=(0.1, 10.0))  # Fornisci un intervallo iniziale

# Estrai il raggio dal risultato
raggio_ottimale = risultato.x

# Calcola l'altezza associata al raggio ottimale
altezza_ottimale = 2 * raggio_ottimale

# Stampare i risultati
print(f"Raggio ottimale: {raggio_ottimale:.2f} unità")
print(f"Altezza ottimale: {altezza_ottimale:.2f} unità")
