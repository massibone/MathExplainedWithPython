'''
Si consideri l’applicazione lineare f : R
4 → R^4 definita da
f (x; y; z; t) = (−x + z; −y + t; x − z; y − t)
perché dim Kerf = 2?

dobbiamo trovare le soluzioni dell'equazione 
f(x,y,z,t)=0.
Può essere scritta come:
  
−x+z=0
−y+t=0
x−z=0
y−t=0
​quindi 
x=z
y=t
​
''' 
from sympy import symbols, Eq, solve

# Definire le variabili
x, y, z, t = symbols('x y z t')

# Definire l'applicazione lineare f
f_x = -x + z
f_y = -y + t
f_z = x - z
f_t = y - t

# Risolvere il sistema di equazioni lineari f(x, y, z, t) = 0
sistema_equazioni = [Eq(f_x, 0), Eq(f_y, 0), Eq(f_z, 0), Eq(f_t, 0)]
soluzioni = solve(sistema_equazioni, (x, y, z, t))

# Calcolare la dimensione del nucleo
dimensione_nucleo = len(soluzioni)

print(f"Le soluzioni del sistema sono: {soluzioni}")
print(f"La dimensione del nucleo di f è: {dimensione_nucleo}")

