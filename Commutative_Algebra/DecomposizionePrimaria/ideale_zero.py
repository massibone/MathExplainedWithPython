
'''
L'ideale zero è come avere una scatola che contiene solo il numero zero. In matematica, l'ideale zero in un anello è l'insieme che contiene solo l'elemento zero.

Divisori dello Zero
Gli elementi divisori dello zero in un anello sono come mattoncini che, quando combinati con altri mattoncini, danno sempre zero. Ad esempio, se moltiplichi un mattoncino rosso con un mattoncino blu e ottieni zero, allora il mattoncino rosso o blu è un divisore dello zero.

Ideali Primi e Decomposizione
Un ideale primo è come una scatola di mattoncini che ha una proprietà molto speciale: ogni volta che combini due mattoncini e il risultato è nella scatola, allora almeno uno dei due mattoncini era già nella scatola.

Quando diciamo che l'ideale zero è decomponibile, significa che possiamo trovare diversi ideali primi tali che, messi insieme, coprono tutti i divisori dello zero.
'''
import sympy as sp

# Definiamo l'anello dei polinomi in due variabili x e y
x, y = sp.symbols('x y')
R = sp.PolyRing([x, y], sp.ZZ)

# Definiamo l'ideale zero
ideal_zero = sp.Ideal(0, domain=R)

# Troviamo i divisori dello zero
zero_divisors = R.zero_divisors()

# Troviamo gli ideali primi appartenenti all'ideale zero
prime_ideals = ideal_zero.associated_primes()

# Visualizziamo i divisori dello zero e gli ideali primi
print("Divisori dello zero:", zero_divisors)
print("Ideali primi appartenenti all'ideale zero:", prime_ideals)
