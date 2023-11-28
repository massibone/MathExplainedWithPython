import numpy as np

# Definisci la permutazione
permutazione = np.array([2, 3, 1])

# Definisci la tripla
tripla = np.array([-1, 0, 1])

# Applica la permutazione alla tripla
risultato = tripla[permutazione - 1]

# Costruisci la matrice risultante
matrice_risultante = np.zeros((len(risultato), len(risultato)))
for i, valore in enumerate(risultato):
    matrice_risultante[i, valore - 1] = 1

print("Matrice risultante:")
print(matrice_risultante)
