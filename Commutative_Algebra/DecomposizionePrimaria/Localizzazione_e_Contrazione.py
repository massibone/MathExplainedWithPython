'''
Parte Moltiplicativa
Una parte moltiplicativa è un gruppo speciale di mattoncini che, quando li usi per costruire, 
ti permettono di ottenere nuovi tipi di mattoncini. Questi nuovi tipi di mattoncini vengono chiamati localizzazione.

Localizzazione e Contrazione
Quando prendi un ideale e usi questi mattoncini moltiplicativi per ottenere nuovi tipi di mattoncini, 
ottieni qualcosa chiamato localizzazione dell'ideale. Se poi vuoi riportare questi nuovi mattoncini al loro stato originale nella scatola, fai una contrazione. 
La contrazione in A dell'ideale localizzato si denota con S(a).
'''

import sympy as sp

# Definiamo l'anello dei polinomi in due variabili x e y
x, y = sp.symbols('x y')
R = sp.PolyRing([x, y], sp.ZZ)

# Definiamo un ideale nell'anello
a = sp.Ideal(x*y, domain=R)

# Definiamo una parte moltiplicativa S
S = [y]

# Calcoliamo la localizzazione di a rispetto a S
S_inverse_a = a.localization(S)

# Calcoliamo la contrazione in A dell'ideale localizzato
S_contraction_a = S_inverse_a.contraction(R)

# Visualizziamo i risultati
print("Ideale a:", a)
print("Localizzazione dell'ideale a rispetto a S:", S_inverse_a)
print("Contrazione in A dell'ideale localizzato:", S_contraction_a)
