'''
sia A un dominio di integrità integralmente chiuso, K il suo capo delle frazioni e L un'estensione finita normale separabile K. 
Sia G il gruppo di Galois di L su K e sia B la chiusura integrale di A in  L. provare che sigma(B)=B per ogni sigma appartenente a G e inoltre che A =B^o
Cos'è un Dominio di Integrità Integralmente Chiuso?
Immagina di avere una collezione di mattoncini LEGO che è perfetta: 
non ci sono mattoncini difettosi e ogni costruzione che fai è stabile e non si rompe mai. 
Questa collezione speciale è chiamata dominio di integrità integralmente chiuso.

Cos'è un Campo delle Frazioni?
Ora, prendi questi mattoncini e pensa di poterli dividere in pezzi più piccoli, 
ma senza ottenere frazioni che non siano mattoncini interi. Questo è come creare un campo delle frazioni della tua collezione di mattoncini.

Cos'è un'Estensione di Campo?
Immagina di trovare un'altra collezione di mattoncini 
che include la tua collezione originale e 
aggiunge nuovi tipi di mattoncini. 
Questo è come avere un'estensione del campo, 
chiamata L.
Gruppo di Galois
Il gruppo di Galois è come un gruppo di maghi che possono fare trasformazioni magiche sulla tua nuova collezione di mattoncini (L) ma che lasciano invariata la tua collezione originale (K).

Chiusura Integrale
La chiusura integrale di una collezione di mattoncini è come trovare 
tutti i mattoncini possibili che possono essere creati combinando in modo speciale i mattoncini originali senza ottenere pezzi rotti.
'''
import sympy as sp
from sympy.abc import x

# Definiamo il campo K come un campo di frazioni dei polinomi su Z
K = sp.FractionField(sp.PolyRing(x, sp.QQ))

# Definiamo un'estensione di campo L come una radice di un polinomio irriducibile su K
L = K.extension(x**2 - 2, 'a')
a = L.gens[0]

# Definiamo il gruppo di Galois G di L su K
G = sp.GaloisGroup(L, K)

# Verifichiamo che sigma(B) = B per ogni sigma in G
B = L.integral_closure()
invariant_under_Galois = all(g(B) == B for g in G)

# Verifichiamo che A = B^0
A = B.normalization()
equals_original = A == L.ring

# Visualizziamo i risultati
print("Campo delle frazioni K:", K)
print("Estensione di campo L:", L)
print("Chiusura integrale B:", B)
print("Invarianza sotto il gruppo di Galois:", invariant_under_Galois)
print("A è uguale alla chiusura integrale di B:", equals_original)
