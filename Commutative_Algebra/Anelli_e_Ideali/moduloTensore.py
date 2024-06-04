import sympy as sp

# Definizione degli anelli e dei moduli
Z = sp.ZZ  # Anello degli interi
m = 4
n = 3
ZmZ = Z.quo(m)  # Anello degli interi modulo m
ZnZ = Z.quo(n)  # Anello degli interi modulo n

# Calcolo del modulo tensore (Z/mZ) ⊗Z (Z/nZ)
tensor_module = sp.tensor_product(ZmZ, ZnZ)

# Verifica se il modulo tensore è uguale a zero
is_zero = tensor_module.is_zero

# Stampiamo il risultato
if is_zero:
    print("Il modulo tensore (Z/{}Z) ⊗Z (Z/{}Z) è uguale a 0.".format(m, n))
else:
    print("Il modulo tensore (Z/{}Z) ⊗Z (Z/{}Z) NON è uguale a 0.".format(m, n))
