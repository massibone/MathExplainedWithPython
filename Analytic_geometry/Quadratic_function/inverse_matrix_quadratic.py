import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# definiamo la variabile simbolica x
x = sp.symbols('x')

# definiamo la funzione quadratica
y = x**2 - 3*x + 5

# definiamo il punto di partenza per la rappresentazione grafica
start_point = -5

# definiamo il punto di arrivo per la rappresentazione grafica
end_point = 5

# definiamo il numero di punti in cui suddividere l'intervallo di rappresentazione
num_points = 100

# calcoliamo i valori della funzione y per ogni punto dell'intervallo di rappresentazione
x_vals = np.linspace(start_point, end_point, num_points)
y_vals = [y.subs(x, i) for i in x_vals]

# definiamo la figura e i suoi assi
fig, ax = plt.subplots()

# disegnamo la funzione
ax.plot(x_vals, y_vals)

# impostiamo le etichette degli assi
ax.set_xlabel('x')
ax.set_ylabel('y')

# impostiamo il titolo del grafico
ax.set_title('Funzione quadratica: y = x^2 - 3x + 5')

# mostraimo la griglia sul grafico
ax.grid()

# mostriamo il grafico
plt.show()
