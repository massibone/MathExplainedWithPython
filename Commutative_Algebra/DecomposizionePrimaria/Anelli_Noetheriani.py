'''
Cos'è un Ideale Primo?
Un ideale primo è come una scatola speciale che ha una proprietà molto particolare: se prendi due mattoncini qualsiasi e il loro prodotto è dentro questa scatola, allora almeno uno dei due mattoncini era già nella scatola.

Ideali Primari
Gli ideali primari sono scatole che, pur essendo speciali, sono un po' meno rigide degli ideali primi. Quando moltiplichi due mattoncini e il risultato è dentro un ideale primario, uno dei mattoncini è quasi sempre dentro un ideale primo associato.

Intersezione di Ideali Primari
Quando prendi l'intersezione di tutti gli ideali primari associati a un ideale primo, ottieni un insieme che può essere rappresentato come 
𝑆
𝑝
(
0
)
S 
p
​
 (0), dove 
𝑆
𝑝
S 
p
​
  è la parte moltiplicativa che esclude gli elementi dell'ideale primo 
𝑝
p.

Anelli Noetheriani
Gli anelli noetheriani sono come scatole di mattoncini che soddisfano certe proprietà di "finitezza". In questi anelli, la definizione che abbiamo visto si verifica sempre.
'''
import sympy as sp

# Definiamo l'anello dei polinomi in due variabili x e y
x, y = sp.symbols('x y')
R = sp.PolyRing([x, y], sp.ZZ)

# Definiamo un ideale primo
p = sp.Ideal(x, domain=R)

# Troviamo i p-primari associati a p
p_primary_ideals = [sp.Ideal(x**2, domain=R), sp.Ideal(x*y, domain=R)]

# Calcoliamo l'intersezione di tutti gli ideali p-primari
intersection_p_primary = p_primary_ideals[0]
for ideal in p_primary_ideals[1:]:
    intersection_p_primary = intersection_p_primary.intersect(ideal)

# Calcoliamo Sp(0)
S_p = [elem for elem in R.gens if not elem in p]
S_p_0 = sp.Ideal(0, domain=R).localization(S_p).contraction(R)

# Verifichiamo se l'intersezione degli ideali p-primari è uguale a Sp(0)
is_equal = intersection_p_primary == S_p_0

# Visualizziamo i risultati
print("Ideale primo p:", p)
print("Ideali p-primari:", p_primary_ideals)
print("Intersezione degli ideali p-primari:", intersection_p_primary)
print("Sp(0):", S_p_0)
print("L'intersezione degli ideali p-primari è uguale a Sp(0):", is_equal)
