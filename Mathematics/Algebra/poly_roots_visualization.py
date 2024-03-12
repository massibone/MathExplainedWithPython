import numpy as np
import matplotlib.pyplot as plt

def poly_roots_visualization(coefficients, xmin, xmax, ymin, ymax, resolution=1000):
    # Calcoliamo le radici del polinomio
    roots = np.roots(coefficients)
    
    # Creiamo una griglia di punti nel piano complesso
    x = np.linspace(xmin, xmax, resolution)
    y = np.linspace(ymin, ymax, resolution)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    
    # Calcoliamo il modulo del polinomio nei punti della griglia
    polynomial_values = np.abs(np.polyval(coefficients, Z))
    
    # Creiamo il plot
    plt.figure(figsize=(10, 8))
    
    # Plot della disposizione delle radici
    plt.scatter(roots.real, roots.imag, color='red', label='Radici del polinomio')
    
    # Plot del modulo del polinomio
    plt.contourf(X, Y, polynomial_values, cmap='viridis')
    plt.colorbar(label='Modulo del polinomio')
    
    plt.xlabel('Parte reale')
    plt.ylabel('Parte immaginaria')
    plt.title('Disposizione delle radici e modulo del polinomio nel piano complesso')
    plt.legend()
    plt.grid(True)
    plt.show()

# Esempio di utilizzo
coefficients = [1, -5, 6]  # Coefficienti del polinomio: x^2 - 5x + 6
xmin, xmax = -3, 5
ymin, ymax = -3, 3
poly_roots_visualization(coefficients, xmin, xmax, ymin, ymax)
