'''
Il teorema del Going-Down dice che se inizi con una costruzione (un ideale primo) in un livello superiore e vuoi scendere a un livello inferiore mantenendo certe regole speciali, puoi sempre trovare un modo per "scendere" senza perdere queste regole. In altre parole, se hai una sequenza di ideali primi e vuoi trovare un ideale primo in un livello inferiore che corrisponda a quello superiore, puoi farlo.
'''
import sympy as sp

# Definiamo un anello dei polinomi in due variabili x e y
S = sp.PolyRing('x y', sp.ZZ)
x, y = S.gens

# Definiamo un ideale primo in S
prime_ideal_S = sp.Ideal(x, domain=S)

# Consideriamo un sottoanello R con una variabile x
R = sp.PolyRing('x', sp.ZZ)
x_R = R.gens[0]

# Definiamo un omomorfismo che mappa S in R
def ring_homomorphism_to_R(f):
    return sp.sympify(f, locals={'x': x_R})

# Troviamo la contrazione dell'ideale primo in R
contraction_prime_ideal_R = prime_ideal_S.contraction(R)

# Verifichiamo se la contrazione è primo in R
is_prime_in_R = contraction_prime_ideal_R.is_prime

# Visualizziamo i risultati
print("Anello S:", S)
print("Ideale primo in S:", prime_ideal_S)
print("Anello R:", R)
print("Contrazione dell'ideale primo in R:", contraction_prime_ideal_R)
print("L'ideale contratto è primo in R:", is_prime_in_R)
