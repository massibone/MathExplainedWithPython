import math

def werner_formula(a, b, C):
# Converte l'angolo da gradi a radianti
    C = math.radians(C)

# Calcola l'angolo A con la formula di Werner
    A = math.degrees(math.asin((a * math.sin(C)) / b))

# Calcola l'angolo restante (B) come somma degli altri due angoli
    B = 180 - A - C

# Calcola la lunghezza del lato mancante (c) con la legge sui coseni
    c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(B)))

    return (A, B, c)

# Esempio 
a = 5
b = 7
C = 30
result = werner_formula(a, b, C)

print("Angolo A: {:.2f}".format(result[0]))
print("Angolo B: {:.2f}".format(result[1]))
print("Lunghezza lato c: {:.2f}".format(result[2]))