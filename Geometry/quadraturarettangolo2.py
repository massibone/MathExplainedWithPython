'''
QUADRATURA RETTANGOLO come lo facevano antichi greci
Il metodo pio semplice è di portare p e q di seguito su una retta, 
d'innalzare una perpendicolare nel loro punto comune (N), e di taglia re 
questa (in C) con una circonferenza di centro O (il punto di mezzo di 
p+q) e passante per i punti estremi A e B di p+q 
Allora la proporzione [I] segue dal fatto che ABC è un triangolo rettangolo e C il 
vertice dell"' angolo alla semicirconferenza "; otteniamo i tre triangoli 
ABC, ACN, CNB geometricamente simili.

'''



import matplotlib.pyplot as plt
import numpy as np

# Definizione dei punti p e q
p = 5
q = 8

# Calcola il punto medio tra p e q
O = (p + q) / 2

# Costruisci un array di punti per rappresentare la retta con p e q
x_points = [0, p, p, 0]
y_points = [0, 0, q, q]

# Costruisci un array di punti per rappresentare la circonferenza
theta = np.linspace(0, np.pi, 100)
r = np.sqrt(p * q)
x_circle = O + r * np.cos(theta)
y_circle = r * np.sin(theta)

# Costruisci un array di punti per rappresentare il triangolo ABC
x_triangle = [0, p, p, 0]
y_triangle = [0, 0, r, r]

# Costruisci un array di punti per rappresentare il triangolo ACN
x_acn = [0, p, O]
y_acn = [0, 0, r]

# Costruisci un array di punti per rappresentare il triangolo CNB
x_cnb = [p, p, O]
y_cnb = [0, r, r]

# Crea il plot
plt.figure(figsize=(8, 8))
plt.plot(x_points, y_points, 'r--', label='Rettangolo p e q')
plt.plot(x_circle, y_circle, 'b', label='Circonferenza ABC')
plt.plot(x_triangle, y_triangle, 'g', label='Triangolo ABC')
plt.plot(x_acn, y_acn, 'y', label='Triangolo ACN')
plt.plot(x_cnb, y_cnb, 'm', label='Triangolo CNB')

# Etichette dei punti
plt.text(p, 0, 'A', ha='left', va='bottom')
plt.text(p, r, 'B', ha='left', va='top')
plt.text(0, 0, 'C', ha='right', va='bottom')

plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Quadratura del Rettangolo')
plt.grid()
plt.show()
