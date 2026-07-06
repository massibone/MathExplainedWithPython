

import math

a = 45 # Esempio di angolo in radianti

# Calcolo della formula sen a/2 = +- sqrt(1 - cos a / 2)
sen_a_2_pos = math.sqrt((1 - math.cos(a / 2)) / 2)
sen_a_2_neg = -math.sqrt((1 - math.cos(a / 2)) / 2)

# Stampo i risultati
print("Angolo in radianti:", a)
print("Valore positivo di sen a/2:", sen_a_2_pos)
print("Valore negativo di sen a/2:", sen_a_2_neg)
