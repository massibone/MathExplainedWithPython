import numpy as np
import matplotlib.pyplot as plt

# Valori di a e b (assicurati che a > b > 0)
a = 3
b = 2

# Calcola la funzione radice n-esima per vari valori di n
n_values = np.arange(1, 1000)  # Scelgo 1000 valori di n
function_values = np.power(a**n_values + b**n_values, 1/n_values)

# Calcola il limite approssimato per grandi n
approximated_limit = function_values[-1]

# Visualizza la funzione per vari valori di n
plt.plot(n_values, function_values, label=r'$\sqrt[n]{a^n + b^n}$')
plt.axhline(y=approximated_limit, color='r', linestyle='--', label='Limite approssimato')

plt.xlabel('n')
plt.ylabel(r'$\sqrt[n]{a^n + b^n}$')
plt.title(r'$\lim_{{n \to \infty}} \sqrt[n]{{a^n + b^n}}$')
plt.legend()
plt.grid(True)
plt.show()

print("Limite approssimato per n grande:", approximated_limit)
