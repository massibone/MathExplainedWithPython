import numpy as np
import matplotlib.pyplot as plt

# Parametri dell'ellisse
a = 3.0  # Semiasse maggiore
b = 2.0  # Semiasse minore

# Equazione dell'ellisse
def ellisse(x):
    return b * np.sqrt(1 - (x**2 / a**2))

# Raggio iniziale
x_start = -a
y_start = 0

# Numero di riflessioni
n_riflessioni = 6

# Creazione del grafico
x = np.linspace(-a, a, 400)
y = ellisse(x)

plt.figure(figsize=(8, 6))

for _ in range(n_riflessioni):
    # Calcola il punto di impatto e la normale all'ellisse
    x_impact = x_start
    y_impact = y_start
    slope_normal = -x_impact / (b**2 / a**2)

    # Calcola il punto di riflessione
    x_reflected = x_impact - 2 * (y_impact - ellisse(x_impact)) * slope_normal
    y_reflected = ellisse(x_reflected)

    # Traccia il raggio incidente e il punto di riflessione
    plt.plot([x_start, x_impact], [y_start, y_impact], 'b')
    plt.plot(x_impact, y_impact, 'bo')
    plt.plot([x_impact, x_reflected], [y_impact, y_reflected], 'r')
    
    # Aggiorna il punto di partenza per la prossima riflessione
    x_start = x_reflected
    y_start = y_reflected

# Traccia l'ellisse
plt.plot(x, y, 'g', linewidth=2, label='Ellisse')

plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Comportamento del raggio dopo {n_riflessioni} riflessioni')
plt.legend()
plt.grid(True)
plt.show()
