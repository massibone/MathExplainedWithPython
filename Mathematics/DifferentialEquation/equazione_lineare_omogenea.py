
'''
Le equazioni lineari omogenee del secondo ordine con coefficienti costanti hanno applicazioni in diversi campi della fisica e dell'ingegneria, come ad esempio:

Modellazione del moto di un corpo oscillante
Studio di circuiti elettrici
Analisi di sistemi dinamici
'''


def equazione_lineare_omogenea(a, b, c, x0, v0, t):
  """
  Risolve l'equazione lineare omogenea del secondo ordine:

  a * y'' + b * y' + c * y = 0

  con condizioni iniziali:

  y(t0) = x0
  y'(t0) = v0

  Parametri:
    a (float): coefficiente di y''
    b (float): coefficiente di y'
    c (float): coefficiente di y
    x0 (float): valore iniziale di y
    v0 (float): valore iniziale di y'
    t (float): tempo

  Restituisce:
    y (float): soluzione dell'equazione
  """

  # Calcolo le radici del polinomio caratteristico
  p = np.poly1d([a, b, c])
  r1, r2 = p.roots

  # Soluzione generale dell'equazione
  if r1 == r2:
    y = (x0 + v0 * t) * np.exp(r1 * t)
  else:
    y = c1 * np.exp(r1 * t) + c2 * np.exp(r2 * t)

  # Calcolo delle costanti c1 e c2 usando le condizioni iniziali
  c1 = x0 - v0 * r1 / (r2 - r1)
  c2 = v0 / (r2 - r1)

  return y

# Esempio di utilizzo
a = 1
b = 2
c = 1
x0 = 1
v0 = 0
t = np.linspace(0, 10, 100)

y = equazione_lineare_omogenea(a, b, c, x0, v0, t)

# Plot della soluzione
import matplotlib.pyplot as plt

plt.plot(t, y)
plt.xlabel("Tempo (t)")
plt.ylabel("Soluzione (y)")
plt.show()
