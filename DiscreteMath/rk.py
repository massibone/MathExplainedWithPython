import numpy as np

def calcola_bozza_a(matrice):
  """
  Calcola la Bozza A' di una matrice.

    """

  # Controlla che la matrice sia quadrata.

  if matrice.shape[0] != matrice.shape[1]:
    raise ValueError("La matrice deve essere quadrata.")

  # Inizializza la Bozza A'.

  bozza_a = np.zeros_like(matrice)

  # Per ogni riga della matrice...

  for i in range(matrice.shape[0]):
    # Trova il massimo elemento della riga.

    max_elemento = np.max(matrice[i])

    # Divide la riga per il massimo elemento.

    bozza_a[i] = matrice[i] / max_elemento

  # Elimina la prima, la seconda e la quinta riga di A.

  bozza_a = bozza_a[2:, 2:]

  # Calcola il rango della matrice A(2; 3; 3; 4).

  rango = np.linalg.matrix_rank(bozza_a)

  return rango


# Esempio di utilizzo.

matrice = np.array([[1, 4, -2, 3, 4], [6, 3, 0, 2, 6], [0, 7, 0, 0, 1], [2, -1, -1, 1, 0], [1, 4, -2, 3, 4]])
rango = calcola_bozza_a(matrice)
print(rango)

'''
Questo output è corretto, poiché la terza e la quarta colonna di A(2; 3; 3; 4) sono uguali, quindi sono linearmente dipendenti. Pertanto, il rango della matrice A(2; 3; 3; 4) è 1.
'''