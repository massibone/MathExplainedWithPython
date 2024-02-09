'''
Sia E l’insieme numerico sull’asse reale R dato da
E={x appartiene a R:x**2-3x+2=0} incluso {x appartiene a R: x**3 - 8 = 0} 
Quali delle seguenti uguaglianze è corretta?
a) E = {1, 2}
b) E = {2}
c) E = ∅ (insieme vuoto)
d) E = {2

'''

L'equazione x^2 - 3x + 2 = 0 può essere fattorizzata in (x - 1)(x - 2) = 0. Quindi, le soluzioni di questa equazione sono x = 1 e x = 2.

L'equazione x^3 - 8 = 0 è l'equazione cubica che può essere fattorizzata in (x - 2)(x^2 + 2x + 4) = 0. Le soluzioni di questa equazione sono x = 2 e le soluzioni complesse che non ci interessano in questo caso.

Ora, consideriamo l'insieme E come l'intersezione di due insiemi:

E = {x appartiene a R: x^2 - 3x + 2 = 0} ∩ {x appartiene a R: x^3 - 8 = 0}

Le soluzioni comuni a entrambe le equazioni sono x = 2. Quindi:

E = {2}
'''

# Importa il modulo sympy per la risoluzione delle equazioni
import sympy as sp

# Definisci la variabile simbolica x
x = sp.symbols('x')

# Risolvi l'equazione x^2 - 3x + 2 = 0
eq1 = x**2 - 3*x + 2
solutions_eq1 = sp.solve(eq1, x)

# Risolvi l'equazione x^3 - 8 = 0
eq2 = x**3 - 8
solutions_eq2 = sp.solve(eq2, x)

# Calcola l'insieme E come l'intersezione delle soluzioni delle due equazioni
E = set(solutions_eq1).intersection(set(solutions_eq2))

# Stampa l'insieme 
print("Insieme E:", E)
