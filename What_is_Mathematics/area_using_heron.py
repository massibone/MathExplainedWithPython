import numpy as np
import matplotlib.pyplot as plt

def calculate_area_using_heron(a, b, c):
    # Calcola il semiperimetro
    s = (a + b + c) / 2
    # Calcola l'area utilizzando il teorema di Erone
    area = np.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Lati del triangolo
a = 8.0
b = 15.0
c = 17.0

# Calcola l'area utilizzando il teorema di Erone
area = calculate_area_using_heron(a, b, c)

# Stampa l'area
print(f'L\'area del triangolo è: {area:.2f} unità quadrate')

# Disegna il triangolo
plt.figure()
plt.plot([0, a], [0, 0], label='Base (a)')
plt.plot([0, 0], [0, c], label='Altezza (c)')
plt.plot([0, a], [0, c], label='Lato (b)')
plt.text(a/2, -1, f'a = {a}', horizontalalignment='center')
plt.text(-1, c/2, f'c = {c}', verticalalignment='center', rotation='vertical')
plt.text(a/2, c/2, f'b = {b}', horizontalalignment='right')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-2, a + 2)
plt.ylim(-2, c + 2)
plt.title('Triangolo con lati a, b, c')
plt.legend()
plt.grid(True)
plt.show()
