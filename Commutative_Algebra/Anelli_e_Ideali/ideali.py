'''
Gli ideali e gli anelli quozienti sono concetti fondamentali dell'algebra che possono essere compresi attraverso un esempio. 
Consideriamo l'anello degli interi Z e l'ideale I = 2Z, che rappresenta tutti i multipli di 2. 

**Esempio di Ideale**: In questo caso, l'insieme I = {..., -4, -2, 0, 2, 4, ...} è un ideale di Z poiché è chiuso rispetto alla somma e al prodotto con qualsiasi elemento di Z. 

**Anello Quoziente**: Costruiamo l'anello quoziente Z/2Z, che consiste nei resti della divisione per 2. 
Quindi, Z/2Z = {0 + 2Z, 1 + 2Z}. Questo anello ha due elementi: il resto 0 e il resto 1.
'''
# Definizione dell'anello degli interi Z
Z = set(range(-10, 11))  # Includiamo numeri da -10 a 10 per scopi illustrativi

# Definizione dell'ideale I = 2Z
I = {x for x in Z if x % 2 == 0}  # Insieme di tutti i multipli di 2

# Costruzione dell'anello quoziente Z/2Z
quotient_ring = {}  # Dizionario per memorizzare gli elementi dell'anello quoziente

for x in Z:
    residue = x % 2
    quotient_ring[x] = residue

print("Anello Quoziente Z/2Z:")
for key, value in quotient_ring.items():
    print(f"Resto di {key} è {value}")


