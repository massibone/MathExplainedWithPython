'''
Certamente! Il problema di Hurwitz riguarda la stabilità di un polinomio, 
ed è solitamente esaminato per determinare se le radici di un polinomio sono tutte a parte reale negativa (o non positiva).
'''
import numpy as np

def hurwitz_criterion(coefficients):
    n = len(coefficients) - 1
    a = np.zeros(n)
    b = np.zeros(n)
    
    # Costruisci le matrici di Hurwitz
    for i in range(n):
        a[i] = coefficients[i+1]
        b[i] = coefficients[i]
    
    hurwitz_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                hurwitz_matrix[i][j] = b[0]
            elif i == j - 1:
                hurwitz_matrix[i][j] = b[i+1]
                
    # Controllo della stabilità
    eigenvalues, _ = np.linalg.eig(hurwitz_matrix)
    if all(eigenvalues < 0):
        print("Tutte le radici sono a parte reale negativa.")
    elif all(eigenvalues <= 0):
        print("Tutte le radici sono a parte reale non positiva.")
    else:
        print("Il polinomio non soddisfa il criterio di Hurwitz.")

# Esempio di utilizzo
coefficients = [1, -2, -3, 4]  # Coefficienti del polinomio: x^3 - 2x^2 - 3x + 4
hurwitz_criterion(coefficients)
