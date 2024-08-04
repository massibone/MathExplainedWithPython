''
Il lemma di Artin-Rees dice che, 
se tagli la pila grande in pezzi 
sempre più piccoli con il coltello 𝐼, 
a un certo punto la pila piccola 𝑁 
si comporta in modo prevedibile rispetto 
ai pezzi della pila grande.
''
import sympy as sp

# Definizione dell'anello noetheriano A e dell'ideale I
A = sp.PolyRing(sp.symbols('x'), domain='ZZ')
x = A.gens[0]
I = A.ideal(x)

# Modulo M e sottomodulo N
M = [A.gens[0]**i for i in range(2)]
N = [A.gens[0]]

def intersection(I, n, M, N):
    # Calcola I^n M
    InM = [I**n * m for m in M]
    # Intersezione con N
    intersection = [n for n in N if n in InM]
    return intersection
