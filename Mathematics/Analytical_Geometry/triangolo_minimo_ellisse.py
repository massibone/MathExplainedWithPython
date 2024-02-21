import math

# Funzione per calcolare il coefficiente angolare della retta passante per due punti
def coefficiente_angolare(x1, y1, x2, y2):
  if x1 == x2:
    return float('inf')
  else:
    return (y2 - y1) / (x2 - x1)

# Funzione per calcolare l'area del triangolo formato da tre punti
def area_triangolo(x1, y1, x2, y2, x3, y3):
  return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

# Funzione per trovare il triangolo di area minima circoscritto a un'ellisse
def triangolo_minimo_ellisse(a, b):
  # Calcola i punti di intersezione tra l'ellisse e l'asse x
  x1 = math.sqrt(a**2 - b**2)
  x2 = -x1

  # Calcola i coefficienti angolari delle tangenti all'ellisse nei punti di intersezione
  m1 = b / a * math.sqrt(a**2 / b**2 - 1)
  m2 = -m1

  # Trova i punti di intersezione tra le tangenti e l'asse y
  y1 = m1 * x1 + b
  y2 = m2 * x2 + b

  # Calcola l'area del triangolo formato dai punti (x1, y1), (x2, y2) e (0, b)
  area_triangolo_minimo = area_triangolo(0, b, x1, y1, x2, y2)

  return area_triangolo_minimo, (x1, y1), (x2, y2)

# Esempio di utilizzo
a = 5 # Semiasse maggiore
b = 3 # Semiasse minore

area_minima, vertici_triangolo = triangolo_minimo_ellisse(a, b)

print("Area minima del triangolo: ", area_minima)
print("Vertici del triangolo: ", vertici_triangolo)

