'''
Il teorema del Going-Up dice che se inizi con una costruzione (un ideale primo) e vuoi costruire qualcosa di più grande mantenendo certe regole, puoi sempre trovare un modo per "salire" mantenendo le proprietà speciali. È come se tu avessi una scala magica che ti permette di salire da un livello di costruzione a un livello superiore senza perdere le regole speciali.
'''
import sympy as sp

# Definiamo un anello dei polinomi in una variabile x
R = sp.PolyRing('x', sp.ZZ)
x = R.gens[0]

# Definiamo un ideale primo in R
prime_ideal_R = sp.Ideal(x, domain=R)

# Estendiamo l'anello aggiungendo una nuova variabile y
S = sp.PolyRing('x y', sp.ZZ)
x, y = S.gens

# Definiamo un omomorfismo che mappa R in S
def ring_homomorphism(f):
    return sp.sympify(f, locals={'x': x, 'y': y})

# Estendiamo l'ideale primo in S
prime_ideal_S = sp.Ideal(ring_homomorphism(prime_ideal_R.gens[0]), domain=S)

# Verifichiamo se prime_ideal_S è primo in S
is_prime = prime_ideal_S.is_prime

# Visualizziamo i risultati
print("Anello R:", R)
print("Ideale primo in R:", prime_ideal_R)
print("Anello S:", S)
print("Estensione dell'ideale primo in S:", prime_ideal_S)
print("L'ideale esteso è primo in S:", is_prime)
