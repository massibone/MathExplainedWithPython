'''
La "quadratura del rettangolo" si riferisce al problema classico di determinare un quadrato con la stessa area di un dato rettangolo. In altre parole, il problema consiste nel trovare un quadrato che ha lo stesso valore dell'area di un rettangolo dato. Questo è un problema di costruzione geometrica che può essere risolto utilizzando strumenti matematici.

Per trovare il lato del quadrato equivalente al rettangolo, puoi seguire questi passaggi:

Supponiamo che il rettangolo abbia una lunghezza di "L" e una larghezza di "W".
Calcola l'area del rettangolo, che è data da A = L * W.
Calcola la radice quadrata dell'area del rettangolo: Lato del quadrato = √(L * W).
Una volta che hai calcolato il lato del quadrato, puoi disegnare il quadrato con lo stesso valore dell'area del rettangolo dato. Questo quadrato avrà la stessa area del rettangolo, ma le sue dimensioni saranno diverse, in quanto sarà un quadrato con lato uguale.

Da notare che la "quadratura del rettangolo" è un concetto diverso dalla "quadratura del cerchio", che è un famoso problema matematico insolubile utilizzando solo riga e compasso.
'''


import matplotlib.pyplot as plt

# Dimensioni del rettangolo
lunghezza_rettangolo = 8
larghezza_rettangolo = 4

# Calcola l'area del rettangolo
area_rettangolo = lunghezza_rettangolo * larghezza_rettangolo

# Calcola il lato del quadrato equivalente
lato_quadrato = area_rettangolo ** 0.5

# Crea una figura
fig, ax = plt.subplots()

# Disegna il rettangolo
rectangle = plt.Rectangle((0, 0), lunghezza_rettangolo, larghezza_rettangolo, color='blue', alpha=0.5)
ax.add_patch(rectangle)

# Disegna il quadrato
square = plt.Rectangle((lunghezza_rettangolo, 0), lato_quadrato, lato_quadrato, color='red', alpha=0.5)
ax.add_patch(square)

# Imposta i limiti dell'asse
ax.set_xlim(0, lunghezza_rettangolo + lato_quadrato)
ax.set_ylim(0, max(larghezza_rettangolo, lato_quadrato))

# Mostra il grafico
plt.axis('equal')
plt.show()
