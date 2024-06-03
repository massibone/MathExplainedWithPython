import sympy as sp

# Definizione degli anelli e moduli
Z = sp.ZZ  # Anello degli interi
B = Z.quo(3)  # Anello dei residui modulo 3
M = Z.quo(2)  # Modulo Z/2Z

# Calcolo del tensore M ⊗_A B
M_tensor_B = sp.tensor_product(M, B)

# Verifica se M ⊗_A B è un B-modulo piatto
def is_flat_module_over_B(module):
    # Verifica se il modulo è piatto utilizzando l'omomorfismo ext
    return all(sp.ext(module, B, i).is_zero for i in range(1, 3))

# Verifica se M ⊗_A B è un B-modulo piatto
is_flat = is_flat_module_over_B(M_tensor_B)

# Stampiamo il risultato
if is_flat:
    print("Il modulo M ⊗_A B è un B-modulo piatto.")
else:
    print("Il modulo M ⊗_A B NON è un B-modulo piatto.")
