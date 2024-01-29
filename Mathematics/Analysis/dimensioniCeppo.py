'''
da un ceppo di legno a sezione trasversale circolare di dato raggio 
vogliamo tagliare una trave avente una sezione trasversale rettanglare 
che offra la massima resistenza alla flessione
'''
'''
Consideriamo il ceppo di legno con una sezione trasversale circolare. 
Se tagliamo una trave rettangolare da questo ceppo, 
la resistenza massima alla flessione si ottiene quando 
il rettangolo è orientato in modo che il suo lato lungo (base) 
sia parallelo all'asse di flessione. In questo caso, 
il momento di inerzia della sezione trasversale rettangolare è 
massimo e uguale a 
1/12bh**3  dove 

b è la base del rettangolo e 

h è l'altezza.
'''
import math

def dimensioni_OttimaliCeppo(raggio):
    # Calcolo delle dimensioni ottimali della sezione trasversale rettangolare
    base_ottimale = 2 * raggio
    altezza_ottimale = math.sqrt(2) * raggio

    return base_ottimale, altezza_ottimale

# Raggio del ceppo di legno

raggio_ceppo = 5.0  # Sostituisci con il valore desiderato

# Calcolo delle dimensioni ottimali
base_ottimale, altezza_ottimale = dimensioni_OttimaliCeppo(raggio_ceppo)

# Stampa dei risultati
print(f"Dimensioni ottimali della sezione trasversale rettangolare:")
print(f"Base: {base_ottimale:.2f}")
print(f"Altezza: {altezza_ottimale:.2f}")
