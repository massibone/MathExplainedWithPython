'''
Un dominio di Dedekind è un dominio d'integrità (un tipo di anello commutativo senza divisori dello zero) con alcune proprietà particolarmente utili:

Ogni ideale frazionario non nullo è invertibile: Questo significa che possiamo "annullare" un ideale frazionario in qualche senso preciso.

Ogni ideale è un prodotto di ideali primi: Ogni ideale (insieme speciale di elementi) può essere scomposto in pezzi fondamentali (ideali primi), che sono come i mattoni di base per costruire altri ideali.

È un anello noetheriano: Significa che non ci sono catene infinite di ideali crescenti, cioè possiamo sempre raggiungere un punto in cui non possiamo aggiungere ulteriori ideali.

È integrally closed: Se un elemento nella frazione del dominio soddisfa un'equazione polinomiale con coefficienti nell'anello, allora l'elemento stesso appartiene all'anello.
'''

import sympy as sp

# Definiamo il dominio di Dedekind come Z[sqrt(-5)]
sqrt_minus_5 = sp.sqrt(-5)
R = sp.Integers(sqrt_minus_5)

# Verifichiamo alcune proprietà
def is_dedekind(domain):
    # Controlliamo alcune proprietà: Noetheriano, ogni ideale frazionario è invertibile, chiuso integralmente
    noetherian = domain.is_noetherian
    integrally_closed = domain.is_integrally_closed
    # Invertibilità degli ideali frazionari e decomposizione in ideali primi sono più complicate da verificare direttamente
    return noetherian and integrally_closed

if is_dedekind(R):
    print(f"L'anello {R} è un dominio di Dedekind.")
else:
    print(f"L'anello {R} non è un dominio di Dedekind.")
