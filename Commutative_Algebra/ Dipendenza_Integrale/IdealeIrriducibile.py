'''
Se 
𝑎
a è un ideale irriducibile in un anello 
𝐴
A, allora le seguenti condizioni sono vere:

a è primario: Questo significa che se un elemento 
𝑥
x non è in 
𝑎
a, allora la localizzazione di 
𝑎
a rispetto a 
𝑥
x è uguale all'annullatore di 
𝑎
a rispetto a 
𝑥
x.

Localizzazione: Per ogni parte moltiplicativa 
𝑆
S di 
𝐴
A, l'anello localizzato 
𝑆
−
1
𝐴
S 
−1
 A è uguale all'annullatore di 
𝑎
a rispetto a qualche 
𝑥
x in 
𝑆
S.

Successione stazionaria: La successione degli ideali 
(
𝑎
:
𝑥
𝑛
)
(a:x 
n
 ) è stazionaria per ogni 
𝑥
x in 
𝐴
A, il che significa che non cambia dopo un certo punto.

Queste condizioni descrivono come un ideale irriducibile 
𝑎
a in un anello 
𝐴
A si comporta in diverse situazioni, come se fosse un giocattolo speciale che ha caratteristiche speciali quando lo usi in modi diversi.

'''
class Ideal:
    def __init__(self, generators):
        self.generators = generators
    
    def is_irreducible(self):
        # Simula la verifica se l'ideale è irriducibile
        return len(self.generators) == 1  # Condizione semplificata per l'esempio

class Ring:
    def __init__(self, name):
        self.name = name
    
    def localize(self, S):
        # Simula la localizzazione dell'anello con la parte moltiplicativa S
        return f"S^-1{self.name}"


# Creazione di un ideale irriducibile a in un anello A
a = Ideal([1])  # Consideriamo un ideale generato da un elemento 1 (semplificazione)

# Verifica se a è irriducibile
print(f"Ideale a è irriducibile?: {a.is_irreducible()}")

# Creazione di un anello A
A = Ring("A")

# Parte moltiplicativa S di A
S = {2, 3, 5}  # Consideriamo una parte moltiplicativa di A

# Localizzazione di A rispetto a S
localized_A = A.localize(S)

print(f"Anello localizzato S^-1A: {localized_A}")
