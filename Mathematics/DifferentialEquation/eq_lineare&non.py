import numpy as np
import matplotlib.pyplot as plt

# Funzione per la soluzione dell'equazione omogenea

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
  if r1 == r2:  # Case of equal roots
    c1 = t * x0 + v0
    c2 = 0  # One constant is enough for equal roots
  else:
    c1 = x0 - v0 * r1 / (r2 - r1)
    c2 = v0 / (r2 - r1)

  # Soluzione generale dell'equazione
  y = c1 * np.exp(r1 * t) + c2 * np.exp(r2 * t)

  return y
# Funzione per la soluzione dell'equazione non omogenea
def equazione_lineare_non_omogenea(a, b, c, f, x0, v0, t):
  """
  Risolve l'equazione lineare non omogenea del secondo ordine:

  a * y'' + b * y' + c * y = f(t)

  con condizioni iniziali:

  y(t0) = x0
  y'(t0) = v0

  Parametri:
    a (float): coefficiente di y''
    b (float): coefficiente di y'
    c (float): coefficiente di y
    f (function): funzione forzante
    x0 (float): valore iniziale di y
    v0 (float): valore iniziale di y'
    t (float): tempo

  Restituisce:
    y (float): soluzione dell'equazione
  """

  # Soluzione generale dell'equazione omogenea
  yh = equazione_lineare_omogenea(a, b, c, x0, v0, t)

  # Soluzione particolare dell'equazione non omogenea
  yp = np.ones_like(t)  # Soluzione particolare da definire in base alla funzione f(t)

  # Soluzione generale dell'equazione non omogenea
  y = yh + yp

  return y

# Esempio di equazione omogenea
a_o = 1
b_o = 2
c_o = 1
x0_o = 1
v0_o = 0
t_o = np.linspace(0, 10, 100)

y_o = equazione_lineare_omogenea(a_o, b_o, c_o, x0_o, v0_o, t_o)

# Esempio di equazione non omogenea
a_n = 1
b_n = 2
c_n = 1
f_n = lambda t: np.sin(t)
x0_n = 1
v0_n = 0
t_n = np.linspace(0, 10, 100)

y_n = equazione_lineare_non_omogenea(a_n, b_n, c_n, f_n, x0_n, v0_n, t_n)

# Grafico
plt.plot(t_o, y_o, label="Omogenea")
plt.plot(t_n, y_n, label="Non omogenea")
plt.xlabel("Tempo (t)")
plt.show()