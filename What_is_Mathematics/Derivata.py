
'''
Quindi, la derivata della funzione radice quadra
[(x+1)/(x-1)] è:

f'(x) = 1/(2x-2)
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 3, 100)

y = np.sqrt(x+1) / (x-1)

dy = 1 / (2*x-2)

plt.plot(x, y, label="f(x)")
plt.plot(x, dy, label="f'(x)")
plt.legend()

plt.show()
