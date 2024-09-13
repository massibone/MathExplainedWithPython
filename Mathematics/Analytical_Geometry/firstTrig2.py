import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Genera i valori x nell'intervallo [-2π, 2π]
xx = np.linspace(-2*np.pi, 2*np.pi, 100)

# Calcola sin(x)
F1 = np.sin(xx)

# Crea il grafico
fig, ax = plt.subplots(figsize=(10, 6))

# Imposta le posizioni e le etichette personalizzate per l'asse x
positions = [np.pi / 2 * x for x in range(-4, 5)]
labels = [r'$-2\pi$', r'$-\frac{3\pi}{2}$', r'$-\pi$', 
          r'$-\frac{\pi}{2}$', 0, r'$\frac{\pi}{2}$', 
          r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$']
ax.xaxis.set_major_locator(ticker.FixedLocator(positions))
ax.xaxis.set_major_formatter(ticker.FixedFormatter(labels))

# Traccia le funzioni
ax.plot(xx, F1, label='sin(x)', color='blue')
ax.axhline(y=1, color='red', linestyle='--', label='cos²(x) + sin²(x) = 1')

# Personalizza il grafico
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Grafico di sin(x) e cos²(x) + sin²(x)')
ax.legend()
ax.grid(True, linestyle=':')

# Visualizza il grafico
plt.tight_layout()
plt.show()
