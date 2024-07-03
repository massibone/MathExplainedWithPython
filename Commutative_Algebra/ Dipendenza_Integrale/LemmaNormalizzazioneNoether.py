'''
Riassunto
Dominio di Integrità: Collezione di mattoncini LEGO senza pezzi difettosi.
Campo delle Frazioni: Possibilità di dividere i mattoncini in pezzi più piccoli.
Estensione di Campo: Aggiungere nuovi tipi di mattoncini alla collezione.
Gruppo di Galois: Maghi che fanno trasformazioni magiche sui mattoncini senza cambiare la collezione originale.
Chiusura Integrale: Trovare tutti i mattoncini possibili creati combinando quelli originali senza pezzi difettosi.
Lemma di Normalizzazione di Noether: 
Organizzare una collezione complessa di mattoncini usando pochi mattoncini di base per costruire tutto il resto.
'''

import sympy as sp

# Definiamo un anello di polinomi in tre variabili su Q
R = sp.PolyRing('x y z', sp.QQ)
x, y, z = R.gens

# Definiamo un ideale generato da polinomi
I = sp.Ideal(x**2 + y**2 - z**2, x**3 - y**3)

# Troviamo i generatori dell'ideale
generators = I.gens

# Visualizziamo i risultati
print("Anello R:", R)
print("Ideale I:", I)
print("Generatori dell'ideale I:", generators)
