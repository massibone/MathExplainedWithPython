def punto_medio_segmentato(x1, y1, x2, y2, rapporto):
  """
  Calcola le coordinate del punto che divide un segmento in un dato rapporto.

  Parametri:
    x1 (float): Coordinata x del primo punto del segmento.
    y1 (float): Coordinata y del primo punto del segmento.
    x2 (float): Coordinata x del secondo punto del segmento.
    y2 (float): Coordinata y del secondo punto del segmento.
    rapporto (float): Rapporto in cui il segmento viene diviso.

  Restituisce:
    tuple: Tupla contenente le coordinate (x, y) del punto di divisione.
  """

  # Calcolo la differenza tra le coordinate dei due punti
  diff_x = x2 - x1
  diff_y = y2 - y1

  # Calcolo le coordinate del punto medio
  x_medio = x1 + (rapporto * diff_x)
  y_medio = y1 + (rapporto * diff_y)

  return x_medio, y_medio

# Esempio di utilizzo
x1, y1 = 1.0, 2.0
x2, y2 = 4.0, 6.0
rapporto = 0.3

x_medio, y_medio = punto_medio_segmentato(x1, y1, x2, y2, rapporto)

print(f"Coordinate del punto di divisione ({rapporto}): ({x_medio}, {y_medio})")


