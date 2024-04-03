import math

# definisci le equazioni
eq1 = [1, math.cos(math.radians(30)), math.sin(math.radians(30)), 6]
eq2 = [math.cos(math.radians(60)), -1, math.sin(math.radians(60)), -2]
eq3 = [math.sin(math.radians(45)), math.cos(math.radians(45)), -1, 3]

# definisci la funzione per calcolare l'angolo aggiunto
def angle_adj(m1, m2):
    return math.degrees(math.atan((m1 - m2) / (1 + m1*m2)))

# calcola gli angoli aggiunti
aa1 = angle_adj(eq1[1], eq2[1])
aa2 = angle_adj(eq1[2], eq3[2])
aa3 = angle_adj(eq2[2], eq3[1])

# calcola le soluzioni
a = eq3[3] / math.sin(math.radians(aa2))
b = eq2[3] / (math.sin(math.radians(aa1)) * math.cos(math.radians(aa2)))
c = eq1[3] / (math.cos(math.radians(aa1)) * math.cos(math.radians(aa3)))

# stampa le soluzioni
print("x =", a)
print("y =", b)
print("z =", c)