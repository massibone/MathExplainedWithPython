#legge reciprocità

def legendre_symbol(a, p):
    """Calcola il simbolo di Legendre (a/p). Restituisce 1 se a è un residuo quadrato modulo p, -1 altrimenti."""
    if a % p == 0:
        return 0  # a è multiplo di p, quindi non è un residuo quadrato
    elif pow(a, (p - 1) // 2, p) == 1:
        return 1  # a è un residuo quadrato modulo p
    else:
        return -1  # a non è un residuo quadrato modulo p

def gauss_reciprocity(p, q):
    """Applica la legge di reciprocità di Gauss per i numeri primi p e q."""
    legendre_p_q = legendre_symbol(p, q)
    legendre_q_p = legendre_symbol(q, p)

    reciprocity_result = legendre_p_q * legendre_q_p * (-1) ** ((p - 1) // 2 * (q - 1) // 2)
    
    return reciprocity_result

# Esempio con p = 5 e q = 11
p = 5
q = 11

# Calcola il simbolo di Legendre per (p/q) e (q/p)
legendre_p_q = legendre_symbol(p, q)
legendre_q_p = legendre_symbol(q, p)

# Applica la legge di reciprocità di Gauss
reciprocity_result = gauss_reciprocity(p, q)

print(f"Simbolo di Legendre ({p}/{q}): {legendre_p_q}")
print(f"Simbolo di Legendre ({q}/{p}): {legendre_q_p}")
print(f"Risultato della legge di reciprocità di Gauss: {reciprocity_result}")
