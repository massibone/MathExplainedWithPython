
'''
dimostrare con python supponiamo di voler trovare tra tutti i rettangoli inscritti in un cerchio di raggio R quello di area massima
'''
from scipy.optimize import minimize

def funzione_obiettivo(dimensions):
    l, w = dimensions
    return -l * w  # Minimizziamo il negativo dell'area per ottenere l'area massima

def vincolo(dimensions, R):
    l, w = dimensions
    return 2 * R - (l**2 + w**2)**0.5  # La diagonale del rettangolo deve essere minore o uguale a 2R

# Raggio del cerchio
R = 5

# Stima iniziale per le dimensioni del rettangolo
initial_dimensions = [R, R]

# Definisci la condizione di vincolo
condizione = {'type': 'ineq', 'fun': vincolo, 'args': (R,)}

# Risolvi il problema di ottimizzazione
risultato = minimize(funzione_obiettivo, initial_dimensions, constraints=condizione)

# Estrai le dimensioni ottimali del rettangolo
dimensioni_ottimali = risultato.x

# Calcola l'area massima del rettangolo
area_massima = -risultato.fun

print("Dimensioni ottimali del rettangolo:", dimensioni_ottimali)
print("Area massima del rettangolo:", area_massima)
