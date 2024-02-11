
from sympy import symbols, limit, oo, sqrt

# Esempio 1: Check se la sequenza converge o diverge
x = symbols('x')
r = limit((1 + 1/x)**x, x, oo)
if r == 0:
    print('La sequenza data non converge ad alcun numero')
else:
    print('La sequenza data converge ad un numero ' + str(r))
# Esempio 2: Check se la sequenza converge o diverge
x = symbols('x')
r = limit((x)**2, x, oo)
if r == oo:
    print('La sequenza data non converge ad alcun numero')
else:
    print('La sequenza data converge ad un numero ' + str(r))

# Esempio 3: Check se la sequenza converge o diverge
x = symbols('x')
r = limit(sqrt(x+1) - sqrt(x), x, oo)
if r == oo:
    print('La sequenza data non converge ad alcun numero')
else:
    print('La sequenza data converge ad un numero ' + str(r))
    
