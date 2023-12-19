'''
L'equazione 
a=v+w rappresenta la somma vettoriale tra due vettori 
Questa operazione combina i due vettori rispettando le regole 
della somma vettoriale.

La somma vettoriale è una operazione che combina vettori 
nello spazio tridimensionale o in spazi vettoriali di dimensioni superiori. 
Nella somma vettoriale 

a=v+w, il vettore risultante a avrà una direzione e un modulo determinati 
dalle componenti di v e w secondo le regole della geometria vettoriale.

Il verso di un vettore indica la direzione in cui il vettore "punta". 
Un vettore può puntare in una direzione specifica nello spazio. 
Per vettori bidimensionali come 
v e w, il verso può essere visualizzato considerando la direzione 
del vettore nel piano xy.

Ad esempio, se il vettore v ha coordinate (3, 2) 
e il vettore w ha coordinate (1, -1), 
possiamo rappresentarli in un grafico. 
rappresentata dalla diagonale del parallelogramma formato dai vettori 
v e w.
'''
import numpy as np
import matplotlib.pyplot as plt

# Vettori v e w
v = np.array([3, 2])
w = np.array([1, -1])

# Somma dei vettori
a = v + w

# Creazione del grafico
plt.figure()

# Aggiungi vettori al grafico
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='r', label='v')
plt.quiver(v[0], v[1], w[0], w[1], angles='xy', scale_units='xy', scale=1, color='b', label='w')
plt.quiver(0, 0, a[0], a[1], angles='xy', scale_units='xy', scale=1, color='g', label='a (v + w)')

# Imposta i limiti del grafico
plt.xlim(-1, 5)
plt.ylim(-3, 3)

# Aggiungi griglia
plt.grid(True)

# Aggiungi etichette degli assi
plt.xlabel('X')
plt.ylabel('Y')

# Aggiungi legenda
plt.legend()

# Mostra il grafico
plt.show()
