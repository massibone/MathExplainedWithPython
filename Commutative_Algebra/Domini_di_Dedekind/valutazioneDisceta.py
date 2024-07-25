'''
Un anello di valutazione discreta (DVR - Discrete Valuation Ring) è un tipo particolare di dominio di Dedekind con alcune proprietà specifiche.
Proprietà di un Anello di Valutazione Discreta
Dominio di integrità: Un DVR è un dominio di integrità, cioè un anello commutativo senza divisori dello zero.
Valutazione discreta: Esiste una funzione di valutazione che assegna un valore intero a ciascun elemento, che riflette un "ordine" tra gli elementi.
Unico ideale massimo: Ha un unico ideale massimo 
𝑚
m, generato da un elemento chiamato uniformizzante.
Noetheriano: Ogni catena crescente di ideali si stabilizza, il che significa che è un anello Noetheriano.
Fattorizzazione unica: Ogni elemento non nullo può essere scritto in modo unico (a meno di unità) come un prodotto di una potenza dell'uniformizzante e un'unità.
'''

import sympy as sp

# Definizione del campo di frazioni di Z, Q
Q = sp.RationalField()

# Definiamo un anello di valutazione discreta, ad esempio Z_p
# Consideriamo p = 5
p = 5
DVR = sp.ZZ.valuation(p)

# Mostriamo alcune proprietà dell'anello di valutazione discreta
def is_dvr(domain, prime):
    try:
        # Verifica se il dominio ha una valutazione discreta
        valuation = domain.valuation(prime)
        # Verifica se il dominio ha un unico ideale massimo
        maximal_ideal = domain.maximal_ideal(prime)
        return valuation is not None and maximal_ideal is not None
    except AttributeError:
        return False

if is_dvr(sp.ZZ, p):
    print(f"L'anello Z localizzato in {p} è un anello di valutazione discreta.")
else:
    print(f"L'anello Z localizzato in {p} non è un anello di valutazione discreta.")

# Output finale
print(f"Anello di valutazione discreta per p = {p}: {DVR}")
