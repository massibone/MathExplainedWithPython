import math

# Definiamo le variabili
a1 = 1
b1 = 2
c1 = 3
a2 = 2
b2 = -1
c2 = math.pi

# Risolviamo il sistema
x = (c1*math.cos(b2) - c2*math.cos(b1)) / (a1*math.cos(b2) - a2*math.cos(b1))
y = (c1*math.sin(b2) - c2*math.sin(b1)) / (a1*math.sin(b2) - a2*math.sin(b1))

# Stampiamo le soluzioni
print("x =", x)
print("y =", y)