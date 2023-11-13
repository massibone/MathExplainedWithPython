'''
Per trovare geometricamente la radice cubica del rapporto q/p, puoi seguire questi passi utilizzando un diagramma:

Disegna una linea retta orizzontale e segna un punto A all'estremità sinistra.

Utilizza un compasso per misurare una distanza proporzionale al rapporto q/p lungo la retta orizzontale da A e segna il punto B. La distanza da A a B dovrebbe essere proporzionale al rapporto q/p.

Ora disegna una linea retta verticale dal punto B verso l'alto e segna il punto C all'estremità superiore di questa linea verticale.

Connetti i punti A e C con una linea retta per formare un triangolo rettangolo ABC.

Ora, la radice cubica del rapporto q/p è rappresentata dalla lunghezza del lato AC del triangolo ABC.

Questo metodo sfrutta la proprietà dei triangoli rettangoli e la geometria per rappresentare la radice cubica del rapporto q/p come una distanza lungo la linea orizzontale tra i punti A e B, e poi calcolata come la lunghezza del lato AC del triangolo. La relazione è basata sulla similità dei triangoli.
'''

import matplotlib.pyplot as plt

# Valori di q e p
q = 8
p = 2

# Calcola il rapporto q/p
ratio = q / p

# Calcola la radice cubica del rapporto
cubic_root = ratio ** (1/3)

# Crea una figura
plt.figure(figsize=(8, 8))

# Disegna una linea orizzontale
plt.plot([0, 1], [0, 0], 'r', label='Rettangolo p')

# Disegna una linea verticale
plt.plot([1, 1], [0, cubic_root], 'b', label='Rettangolo q')

# Disegna una linea obliqua
plt.plot([0, 1], [0, cubic_root], 'g--', label='Radice cubica')

# Etichette dei punti
plt.text(0, -0.1, 'A', ha='center', va='top')
plt.text(1, -0.1, 'B', ha='center', va='top')
plt.text(1.1, cubic_root / 2, 'C', ha='left', va='center')

plt.legend()
plt.title('Calcolo geometrico della radice cubica del rapporto q/p')
plt.grid()
plt.show()

# Stampa il valore della radice cubica
print(f"Radice cubica di q/p = {cubic_root}")
