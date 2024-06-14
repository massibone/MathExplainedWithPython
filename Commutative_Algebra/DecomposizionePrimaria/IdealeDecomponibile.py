'''
Un ideale decomponibile è come una scatola di mattoncini che puoi dividere in più scatole più piccole, 
e ogni scatola più piccola è una "parte" importante della scatola originale. 
Ad esempio, se hai una scatola di mattoncini che contiene tutti i mattoncini rossi e blu,
potresti essere in grado di dividerla in una scatola di soli mattoncini rossi e una di soli mattoncini blu.

Ideale Primo Minimale
Un ideale primo minimale è una scatola molto speciale che non può essere divisa ulteriormente in scatole più piccole 
che seguono le regole degli ideali. È come un mattoncino fondamentale che non può essere scomposto in parti più piccole. 
Se hai una scatola che contiene mattoncini fondamentali, ogni scatola di questo tipo è un ideale primo minimale.
'''
import sympy as sp

# Definiamo l'anello dei polinomi in due variabili x e y
x, y = sp.symbols('x y')
R = sp.PolyRing([x, y], sp.ZZ)

# Definiamo un ideale decomponibile
ideal_decomposable = sp.Ideal(x**2 - y, x*y, domain=R)

# Decomposizione primaria dell'ideale decomponibile
primary_decomposition = ideal_decomposable.primary_decomposition()

# Definiamo un ideale primo minimale
ideal_prime_minimal = sp.Ideal(x, domain=R)

# Visualizziamo gli ideali e la loro decomposizione
print("Ideale decomponibile:", ideal_decomposable)
print("Decomposizione primaria dell'ideale decomponibile:", primary_decomposition)
print("Ideale primo minimale:", ideal_prime_minimal)
