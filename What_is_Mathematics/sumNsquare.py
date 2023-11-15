'''
La somma dei primi 
n quadrati può essere dimostrata usando il principio di induzione matematica
'''

import matplotlib.pyplot as plt

def sum_of_squares(n):
    return (n * (n + 1) * (2 * n + 1)) / 6

# Calcola la somma dei primi n quadrati
n_values = list(range(1, 11))  # Calcola per i primi 10 valori di n
sums = [sum_of_squares(n) for n in n_values]

# Visualizza il risultato
plt.plot(n_values, sums, marker='o')
plt.xlabel('n')
plt.ylabel('Somma dei primi n quadrati')
plt.title('Somma dei primi n quadrati')
plt.grid(True)
plt.show()
