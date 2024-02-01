
'''
 funzioni x^3,radice quadrata di x, 
 sin x, 
 sin 2x, 
 sin(x+pi greco/4), 
 ln x, 
 ln(1+x), 
 |x-3|,
 (x+|x|)/2
'''


import numpy as np
import matplotlib.pyplot as plt

# Definizione delle funzioni
def funzione1(x):
    return x**3

def funzione2(x):
    return np.sqrt(x)

def funzione3(x):
    return np.sin(x)

def funzione4(x):
    return np.sin(2*x)

def funzione5(x):
    return np.sin(x + np.pi/4)

def funzione6(x):
    return np.log(x)

def funzione7(x):
    return np.log(1 + x)

def funzione8(x):
    return np.abs(x - 3)

def funzione9(x):
    return (x + np.abs(x)) / 2

# Intervallo di valori x
x_vals = np.linspace(0.01, 5, 400)

# Creazione dei subplot per visualizzare le funzioni
fig, axs = plt.subplots(3, 3, figsize=(15, 15))

# Disegno delle funzioni
axs[0, 0].plot(x_vals, funzione1(x_vals))
axs[0, 0].set_title('x^3')

axs[0, 1].plot(x_vals, funzione2(x_vals))
axs[0, 1].set_title('sqrt(x)')

axs[0, 2].plot(x_vals, funzione3(x_vals))
axs[0, 2].set_title('sin(x)')

axs[1, 0].plot(x_vals, funzione4(x_vals))
axs[1, 0].set_title('sin(2x)')

axs[1, 1].plot(x_vals, funzione5(x_vals))
axs[1, 1].set_title('sin(x + π/4)')

axs[1, 2].plot(x_vals, funzione6(x_vals))
axs[1, 2].set_title('ln(x)')

axs[2, 0].plot(x_vals, funzione7(x_vals))
axs[2, 0].set_title('ln(1 + x)')

axs[2, 1].plot(x_vals, funzione8(x_vals))
axs[2, 1].set_title('|x - 3|')

axs[2, 2].plot(x_vals, funzione9(x_vals))
axs[2, 2].set_title('(x + |x|)/2')

# Impostazioni aggiuntive
for ax in axs.flat:
    ax.grid(True)
    ax.axhline(0, color='black',linewidth=0.5)
    ax.axvline(0, color='black',linewidth=0.5)

plt.tight_layout()
plt.show()
