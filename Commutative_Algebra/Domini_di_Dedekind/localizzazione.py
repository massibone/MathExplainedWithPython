'''
Useremo un anello di Dedekind astratto e illustreremo la localizzazione
'''
import sympy as sp
from sympy.abc import x

# Definiamo un dominio di Dedekind astratto
# In questo esempio usiamo il dominio degli interi algebrici in Q(sqrt(-5))
A = sp.QQ.algebraic_field(x**2 + 5)

# Definiamo una parte moltiplicativa di A
# Sia S l'insieme di tutti gli elementi non nulli di A
# In sympy, possiamo rappresentare una parte moltiplicativa come il set di tutti gli elementi tranne lo zero
S = {a for a in A if a != 0}

# Funzione per localizzare l'anello
def localize_ring(domain, multiplicative_set):
    localized_elements = {domain(r).invertible_element() for r in multiplicative_set if domain(r).is_invertible}
    localized_ring = sp.Frac(domain, localized_elements)
    return localized_ring

# Localizziamo il dominio di Dedekind rispetto a S
localized_A = localize_ring(A, S)

# Verifichiamo alcune proprietà della localizzazione
is_dedekind_localized = localized_A.is_dedekind
print(f"L'anello localizzato è un dominio di Dedekind: {is_dedekind_localized}")

# Output finale
print(f"Anello original: {A}")
print(f"Anello localizzato: {localized_A}")
