'''
Supponiamo di avere l'insieme di vettori (v1, v2, v3) in uno spazio tridimensionale:

v1 = (1, 2, 3)
v2 = (4, 5, 6)
v3 = (7, 8, 9)

Ora consideriamo una sommatoria pesata di questi vettori:

Σ_{k=1}^{3} ak * vk

Dove "ak" sono coefficienti scalari. Ad esempio, supponiamo di prendere i seguenti coefficienti:
(I "coefficienti scalari" sono semplicemente dei numeri reali o complessi che vengono utilizzati per ponderare o moltiplicare i vettori in una combinazione lineare.)
a1 = 2
a2 = -1
a3 = 3

Allora la sommatoria diventerebbe:

2 * v1 - 1 * v2 + 3 * v3

Ora calcoliamo questa combinazione lineare:

2 * (1, 2, 3) - 1 * (4, 5, 6) + 3 * (7, 8, 9)

Ottieni il risultato seguente:

(2, 4, 6) - (4, 5, 6) + (21, 24, 27)

Ora somma questi vettori componente per componente:

(2 - 4 + 21, 4 - 5 + 24, 6 - 6 + 27)

Il risultato è:

(19, 23, 27)

Quindi, la somma pesata 2 * v1 - 1 * v2 + 3 * v3 è una combinazione lineare dei vettori (v1, v2, v3) e il risultato è il vettore (19, 23, 27).

Questa dimostra che la sommatoria con coefficienti scalari è una combinazione lineare dei vettori dati.

'''

import numpy as np

# Definisci i vettori
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
v3 = np.array([7, 8, 9])

# Definisci i coefficienti
a1 = 2
a2 = -1
a3 = 3

# Calcola la combinazione lineare
result = a1 * v1 + a2 * v2 + a3 * v3

print("La combinazione lineare è:", result)
