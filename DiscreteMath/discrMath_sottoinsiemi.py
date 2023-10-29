'''
L'insieme delle parti di un insieme E, denotato come P(E) o 2^E, è l'insieme di tutti i sottoinsiemi di E, inclusi l'insieme vuoto e l'insieme E stesso.

Insieme E è:

E = {0, 1, -1}

Ora possiamo trovare l'insieme delle parti P(E) come segue:

1. Insieme vuoto: ∅
2. Sottoinsiemi con un solo elemento:
   - {0}
   - {1}
   - {-1}
3. Sottoinsiemi con due elementi:
   - {0, 1}
   - {0, -1}
   - {1, -1}
4. Insieme E stesso: {0, 1, -1}

Quindi, l'insieme delle parti P(E) è dato da:

P(E) = {∅, {0}, {1}, {-1}, {0, 1}, {0, -1}, {1, -1}, {0, 1, -1}}
'''
import itertools
# Definisci l'insieme E
E = {0, 1, -1}

# Calcola l'insieme delle parti P(E)
parti_di_E = []

# Genera tutti i sottoinsiemi di E
for i in range(len(E) + 1):
    sottoinsiemi = itertools.combinations(E, i)
    for sottoinsieme in sottoinsiemi:
        parti_di_E.append(set(sottoinsieme))

# Aggiungi l'insieme E stesso
parti_di_E.append(E)

# Stampa l'insieme delle parti P(E)
for insieme in parti_di_E:
    print(insieme)
