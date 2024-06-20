'''
sia A un anello di valutazione di un campo K. Dimostrare che ogni subanello di K che contiene A è un anello locale di A

Dobbiamo dimostrare che ogni sottoanello di 
K che contiene A è un anello locale di A.

'''
import sympy as sp

# Definizione del campo K e del suo anello di valutazione A
K = sp.QQ
A = sp.PolyRing('x', K)
x = A.gens[0]

# Definizione di un ideale in A
ideal = sp.Ideal(x**2 - 1, domain=A)

# Verifica delle proprietà dell'anello di valutazione
print("Anello A:", A)
print("Campo K:", K)
print("Ideale in A:", ideal)

# Calcolo dell'ideale massimale
maximal_ideal = ideal.associated_primes()
print("Ideale massimale:", maximal_ideal)

# Definizione di un sottoanello B che contiene A
B = sp.PolyRing('x', K)
y = B.gens[0]

# Verifica delle proprietà del sottoanello
print("\nSottoanello B che contiene A:", B)
