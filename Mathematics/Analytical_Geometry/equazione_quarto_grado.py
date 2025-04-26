def equazione_quarto_grado(a, b, c, d, e):
  """
  Risolve un'equazione di quarto grado.

  Parametri:
    a (float): Coefficiente di x^4.
    b (float): Coefficiente di x^3.
    c (float): Coefficiente di x^2.
    d (float): Coefficiente di x.
    e (float): Termine noto.

  Restituisce:
    list: Lista contenente le soluzioni 
    dell'equazione.
  """

  # Calcolo del discriminante di Eulero
  F = (3 * b - a**2) / 8

  # Calcolo del discriminante di Cartesio
  G = (4 * c - b**2) / 8

  # Se il discriminante di Eulero è positivo, l'equazione ha quattro soluzioni reali
  if F > 0:
    return equazione_terzo_grado(a / 4, F / 2, G / 2, e / 4)

  # Se il discriminante di Eulero è uguale a zero, l'equazione ha due soluzioni reali e due doppie
  elif F == 0:
    return equazione_terzo_grado(a / 4, F / 2, G / 2, e / 4) + [(-b / 2) / a] * 2

  # Se il discriminante di Eulero è negativo, l'equazione ha quattro soluzioni complesse
  else:
    p = -b / (4 * a)
    q = np.sqrt(-F) / (2 * a)
    theta = np.arccos(-q / p)
    return [
      2 * p * np.cos(theta / 4) - b / (4 * a),
      2 * p * np.cos((theta + 2 * np.pi) / 4) - b / (4 * a),
      2 * p * np.cos((theta + 4 * np.pi) / 4) - b / (4 * a),
      2 * p * np.cos((theta + 6 * np.pi) / 
