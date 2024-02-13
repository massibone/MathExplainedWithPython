'''
dobbiamo trovare le dimensioni ottimali della scatola di latta (senza coperchio) 
che massimizzano il volume dato che si vuole utilizzare la minor quantità possibile di materiale.
'''

from sympy import symbols, solve, diff, Eq

# Definiamo le variabili simboliche
x, y, h, V, lambda_ = symbols('x y h V lambda')

# Definiamo la funzione lagrangiana
L = 2*x*y + 2*x*h + 2*y*h + lambda_*(V - x*y*h)

# Deriviamo parzialmente la funzione lagrangiana rispetto a x, y, h e lambda
dL_dx = diff(L, x)
dL_dy = diff(L, y)
dL_dh = diff(L, h)
dL_dlambda = diff(L, lambda_)

# Risolviamo il sistema di equazioni
sol = solve((dL_dx, dL_dy, dL_dh, dL_dlambda), (x, y, h, lambda_))

# Estraiamo le soluzioni
sol_x = sol[x]
sol_y = sol[y]
sol_h = sol[h]

# Stampiamo le dimensioni ottimali della scatola di latta
print("Dimensione ottimale x:", sol_x)
print("Dimensione ottimale y:", sol_y)
print("Dimensione ottimale h:", sol_h)
