'''
questo programma utilizza il calcolo integrale per determinare il lavoro prodotto da un gas in espansione, conoscendo la legge di variazione della pressione. 
'''
import numpy as np
from scipy.integrate import quad

# Definizione della legge di variazione della pressione (usiamo l'equazione dei gas ideali)
def pressione(V):
    return n * R * T / V

# Definizione della funzione del lavoro
def lavoro(V):
    return -pressione(V)

# Parametri del gas
n = 1.0  # Quantità di sostanza
R = 8.314  # Costante dei gas (J/(mol*K))
T = 300.0  # Temperatura in Kelvin

# Volumi iniziale e finale
V1 = 1.0  # Volume iniziale
V2 = 5.0  # Volume finale

# Calcolo del lavoro utilizzando l'integrazione numerica
risultato, errore = quad(lavoro, V1, V2)

# Stampare il risultato
print(f"Il lavoro compiuto dal gas durante l'espansione è: {risultato:.2f} Joule")

