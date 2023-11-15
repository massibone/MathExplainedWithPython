import numpy as np
import matplotlib.pyplot as plt

def calculate_max_area(a, b):
    # Calcola l'altezza massima
    h = np.sqrt(b**2 - (a/2)**2)
    # Calcola l'area massima
    max_area = 0.5 * a * h
    return max_area

# Lati fissi
b = 10.0  # Latitudine
a_values = np.linspace(0.1, b, 500)  # Varia la base a tra 0.1 e b

# Calcola le aree per i vari valori di a
areas = 0.5 * a_values * np.sqrt(b**2 - (a_values/2)**2)

# Trova il valore di a che massimizza l'area
max_area_index = np.argmax(areas)
a_max_area = a_values[max_area_index]
max_area = areas[max_area_index]

# Plot dell'area in funzione di a
plt.plot(a_values, areas, label='Area del triangolo')
plt.axvline(x=a_max_area, color='r', linestyle='--', label='Base per area massima')
plt.xlabel('Base (a)')
plt.ylabel('Area')
plt.title('Area massima del triangolo con base a e latitudine b')
plt.legend()
plt.grid(True)
plt.show()

print(f'Base (a) per area massima: {a_max_area:.2f}')
print(f'Altezza (h): {np.sqrt(b**2 - (a_max_area/2)**2):.2f}')
print(f'Area massima: {max_area:.2f}')
