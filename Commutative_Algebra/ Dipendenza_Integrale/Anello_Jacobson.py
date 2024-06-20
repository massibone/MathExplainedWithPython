'''
Un anello di Jacobson è un tipo speciale di anello in algebra commutativa. Un anello è come un insieme di numeri o oggetti (come i mattoncini LEGO) con alcune regole su come combinarli. L'anello di Jacobson ha delle proprietà speciali che lo rendono molto interessante e utile in matematica.

Tre Proprietà Equivalenti di un Anello di Jacobson
Esistono tre proprietà importanti che, se soddisfatte, fanno sì che un anello sia un anello di Jacobson. Vediamo quali sono queste proprietà.

Proprietà 1: Gli Ideali Massimali Contengono Ogni Ideale Primo
Pensa agli ideali come a dei sottoinsiemi speciali dei tuoi mattoncini LEGO. Un ideale primo è come un gruppo di mattoncini molto speciale che non può essere diviso ulteriormente. Un ideale massimale è il gruppo più grande di mattoncini che rispetta ancora le regole dell'anello. La prima proprietà dice che ogni gruppo speciale di mattoncini (ideale primo) è contenuto in uno di questi gruppi più grandi (ideale massimale).

Proprietà 2: Il Radicale di Jacobson di A Contiene Ogni Ideale Primo
Il radicale di Jacobson è come un insieme speciale di mattoncini che rappresenta il cuore della tua scatola. La seconda proprietà dice che questo cuore contiene tutti i gruppi speciali di mattoncini (ideali primi).

Proprietà 3: Ogni Ideale Primo è l'Intersezione di Ideali Massimali
La terza proprietà dice che puoi ottenere ogni gruppo speciale di mattoncini (ideale primo) intersecando diversi gruppi più grandi di mattoncini (ideali massimali). È come se tu potessi costruire qualsiasi cosa speciale combinando diversi gruppi grandi di mattoncini.
'''

import sympy as sp

# Definizione di un anello commutativo A
A = sp.PolyRing('x', sp.QQ)
x = A.gens[0]

# Definizione di alcuni ideali in A
I1 = sp.Ideal(x**2 - 1, domain=A)  # Ideale generato da x^2 - 1
I2 = sp.Ideal(x**3 - 1, domain=A)  # Ideale generato da x^3 - 1

# Calcolo degli ideali primi contenuti negli ideali
primes_I1 = I1.associated_primes()
primes_I2 = I2.associated_primes()

# Calcolo degli ideali massimali
maximals = [sp.Ideal(x - a, domain=A) for a in sp.roots(x**2 - 1, A)]

# Verifica delle proprietà
property1_I1 = all(any(maximal.contains(prime) for maximal in maximals) for prime in primes_I1)
property2_I1 = all(prime in sp.radical_jacobson(A) for prime in primes_I1)
property3 = all(any(maximal.contains(prime) for prime in primes_I1) for maximal in maximals)

# Visualizzazione dei risultati
print("Anello A:", A)
print("\nIdeale I1:", I1)
print("Ideale I2:", I2)

print("\nIdeali primi contenuti in I1:", primes_I1)
print("Ideali primi contenuti in I2:", primes_I2)
print("\nIdeali massimali in A:", maximals)

print("\nProprietà 1 (ogni ideale primo è l'intersezione degli ideali massimali che lo contengono) per I1:", property1_I1)
print("Proprietà 2 (il radicale di Jacobson contiene tutti gli ideali primi) per I1:", property2_I1)
print("Proprietà 3 (ogni ideale massimale contiene un ideale primo) per A:", property3)
