'''
Il teorema fondamentale dell'algebra afferma che ogni polinomio complesso di grado n ha esattamente n radici complesse (contando le molteplicità) e quindi può essere scritto come il prodotto di 
n fattori lineari della forma 
(x−r i), dove ri  sono le radici del polinomio.

In generale, il modulo di un polinomio può crescere allontanandosi dall'origine a causa del contributo delle sue radici. 
p(x)=(x−1)(x−2)(x−3).  il polinomio si allontana dall'origine a causa del contributo dei fattori lineari 
'''
import numpy as np
import matplotlib.pyplot as plt

# Definiamo il polinomio
def polynomial(x):
    return (x - 1)*(x - 2)*(x - 3)

# Definiamo l'intervallo
x_values = np.linspace(-2, 5, 1000)

# Calcoliamo il valore del polinomio per ogni punto nell'intervallo
y_values = polynomial(x_values)

# Plot del modulo del polinomio
plt.plot(x_values, np.abs(y_values))
plt.title('Modulo del polinomio (|p(x)|)')
plt.xlabel('x')
plt.ylabel('|p(x)|')
plt.grid(True)
plt.show()

