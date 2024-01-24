'''
Il problema delle quadrature e il problema delle tangenti 
sono legati attraverso il calcolo differenziale e l'integrazione. 
Possiamo dimostrare ciò utilizzando un esempio specifico in Python. 
Consideriamo una funzione e il problema di trovare l'area sotto la curva, 
che è un problema di quadratura. Poi, consideriamo il problema 
di trovare la tangente alla curva in un punto specifico.

f(x)=x**2. La sua derivata, 
f′(x), rappresenta la pendenza della tangente in un punto dato
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Definizione della funzione
def funzione(x):
    return x**2

# Calcolo della derivata
def derivata(x):
    return 2 * x

# Creazione di un intervallo di valori x
x_valori = np.linspace(0, 3, 100)

# Calcolo dei valori della funzione e della derivata
y_funzione = funzione(x_valori)
y_derivata = derivata(x_valori)

# Plot della funzione e della sua derivata
plt.figure(figsize=(10, 6))
plt.plot(x_valori, y_funzione, label='Funzione $f(x) = x^2$')
plt.plot(x_valori, y_derivata, label='Derivata $f\'(x) = 2x$', linestyle='dashed')

# Aggiungi una linea tratteggiata orizzontale per evidenziare il punto di interesse
punto_interesse_x = 2
punto_interesse_y = funzione(punto_interesse_x)
plt.axvline(punto_interesse_x, color='red', linestyle='--', label=f'Punto di interesse x={punto_interesse_x}')
plt.axhline(punto_interesse_y, color='red', linestyle='--', label=f'Punto di interesse y={punto_interesse_y}')

plt.title('Funzione e Derivata')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.show()

# Problema delle quadrature: Calcolo dell'area sotto la curva tra x=0 e x=punto_interesse_x
area_sotto_curva, _ = quad(funzione, 0, punto_interesse_x)
print(f'Area sotto la curva: {area_sotto_curva:.2f}')

# Problema delle tangenti: Calcolo della pendenza della tangente in x=punto_interesse_x
pendenza_tangente = derivata(punto_interesse_x)
print(f'Pendenza della tangente in x={punto_interesse_x}: {pendenza_tangente:.2f}')

from scipy.integrate import quad

# Problema delle quadrature: Calcolo dell'area sotto la curva tra x=0 e x=2
area_sotto_curva, _ = quad(funzione, 0, 2)
print(f'Area sotto la curva: {area_sotto_curva:.2f}')

# Problema delle tangenti: Calcolo della pendenza della tangente in x=1
pendenza_tangente = derivata(1)
print(f'Pendenza della tangente in x=1: {pendenza_tangente:.2f}')
'''
Questo codice calcola l'area sotto la curva della funzione tra 
x=0 e x=2 utilizzando il metodo delle quadrature e calcola la pendenza della tangente nel punto 
utilizzando la derivata. 
Vedrai che l'area sotto la curva è correlata alla pendenza della tangente nel punto di interesse, sottolineando la connessione tra i problemi delle quadrature e 
delle tangenti attraverso il calcolo differenziale e l'integrazione
'''