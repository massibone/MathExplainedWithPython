def punto_intersezione_rette(x1, y1, m1, x2, y2, m2):
  """
  Calcola le coordinate del punto di intersezione di due rette.

  Parametri:
    x1 (float): Coordinata x del primo punto della prima retta.
    y1 (float): Coordinata y del primo punto della prima retta.
    m1 (float): Pendenza della prima retta.
    x2 (float): Coordinata x del primo punto della seconda retta.
    y2 (float): Coordinata y del primo punto della seconda retta.
    m2 (float): Pendenza della seconda retta.

  Restituisce:
    tuple: Tupla contenente le coordinate (x, y) del punto di intersezione.
  """

  # Se le rette sono parallele, non c'è intersezione
  if m1 == m2:
    return None

  # Calcolo la coordinata x del punto di intersezione
  x_intersezione = (m2 * x1 - m1 * x2 + y2 - y1) / (m2 - m1)

  # Calcolo la coordinata y del punto di intersezione
  y_intersezione = m1 * (x_intersezione - x1) + y1

  return x_intersezione, y_intersezione

# Esempio di utilizzo
x1, y1 = 1.0, 2.0
m1 = 3.0
x2, y2 = 4.0, 6.0
m2 = 2.0

x_intersezione, y_intersezione = punto_intersezione_rette(x1, y1, m1, x2, y2, m2)

print(f"Coordinate del punto di intersezione: ({x_intersezione}, {y_intersezione})")
