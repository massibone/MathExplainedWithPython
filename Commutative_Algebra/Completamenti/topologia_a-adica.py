'''
La topologia a-adica è una struttura fondamentale nell'algebra commutativa che permette di studiare 
la convergenza di sequenze e serie in un contesto algebrico. Viene utilizzata per definire 
una nozione di "vicinanza" tra elementi di un anello o modulo, utilizzando un ideale 𝑎 come base per la topologia.
'''
def p_adic_distance(x, y, p):
    """Calcola la distanza p-adica tra x e y."""
    n = 0
    while (x - y) % (p ** (n + 1)) == 0:
        n += 1
    return n

def is_p_adic_convergent(sequence, p):
    """Verifica se una sequenza converge nella topologia p-adica."""
    for n in range(len(sequence) - 1):
        if p_adic_distance(sequence[n], sequence[n + 1], p) < n + 1:
            return False
    return True
# Esempio di sequenza negli interi
sequence = [1, 1 + 3, 1 + 3 + 3**2, 1 + 3 + 3**2 + 3**3]

# Numero primo p
p = 3

# Verifica della convergenza nella topologia p-adica
print(f"La sequenza converge nella topologia {p}-adica?", is_p_adic_convergent(sequence, p))
