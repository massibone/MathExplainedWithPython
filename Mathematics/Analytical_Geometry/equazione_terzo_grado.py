'''
Programma Python per la risoluzione di equazioni algebriche di terzo
'''
def equazione_terzo_grado(a, b, c, d):
  """
  Risolve un'equazione di terzo grado.

  Parametri:
    a (float): Coefficiente di x^3.
    b (float): Coefficiente di x^2.
    c (float): Coefficiente di x.
    d (float): Termine noto.

  Restituisce:
    list: Lista contenente le soluzioni dell'equazione.
  """

  # Calcolo del discriminante
  delta = b**2 - 3 * a * c

  # Se il discriminante è positivo, l'equazione ha tre soluzioni reali
  if delta > 0:
    return [
      (-b + np.sqrt(delta)) / (3 * a),
      (-b - np.sqrt(delta)) / (3 * a),
      (-b) / (3 * a)
    ]

  # Se il discriminante è uguale a zero, l'equazione ha una soluzione reale e una doppia
  elif delta == 0:
    return [-b / (3 * a), -b / (3 * a)]

  # Se il discriminante è negativo, l'equazione ha tre soluzioni complesse
  else:
    p = -b / (3 * a)
    q = np.sqrt(-delta) / (3 * a)
    theta = np.arccos(-q / p)
    return [
      2 * p * np.cos(theta / 3) - b / (3 * a),
      2 * p * np.cos((theta + 2 * np.pi) / 3) - b / (3 * a),
      2 * p * np.cos((theta + 4 * np.pi) / 3) - b / (3 * a)
    ]

# Esempio di utilizzo
a, b, c, d = 1, 2, -3, -4

soluzioni = equazione_terzo_grado(a, b, c, d)

print(f"Soluzioni dell'equazione di terzo grado: {soluzioni}")
