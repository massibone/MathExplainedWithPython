'''
genera istogramma da immagine vettorizzata.
L'istogramma dell'immagine viene calcolato, contando il numero di pixel per ogni livello di intensità
'''
import numpy as np
import matplotlib.pyplot as plt

# Simula un'immagine di esempio
immagine = np.random.rand(100, 100)  # Array casuale con valori tra 0 e 1

# Trasformata di Hilbert 2D
trasformata_hilbert = np.fft.fft2(immagine)  # Utilizzo fft2 per la trasformazione

# Ampiezza della trasformata
ampiezza = np.abs(trasformata_hilbert)

# Istogramma dell'ampiezza
plt.hist(ampiezza.ravel(), bins=256, range=(0, 1))
plt.xlabel("Ampiezza")
plt.ylabel("Conteggio pixel")
plt.title("Istogramma dell'ampiezza della trasformata di Hilbert")
plt.show()


