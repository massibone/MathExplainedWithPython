'''
l'esponenziazione modulare di 5^22 mod 23
è uguale a 1
confermando il teorema di Fermat per 

p=23 e a=5
'''
def modulo_power(base, exponent, modulus):
    result = 1
    base = base % modulus  # Per gestire grandi numeri
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1  # Divisione intera per 2
        base = (base * base) % modulus
    return result

# Dati
p = 23  # Numero primo
a = 5   # Base

# Calcola a^(p-1) modulo p
result = modulo_power(a, p-1, p)

# Verifica se il risultato è 1 (teorema di Fermat)
is_fermat_theorem_valid = result == 1

print(f'5^{p-1} ≡ {result} (mod {p})')
print('Il teorema di Fermat è valido:', is_fermat_theorem_valid)
