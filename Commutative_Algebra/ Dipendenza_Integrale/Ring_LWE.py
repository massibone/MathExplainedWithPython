'''
questo esempio, utilizzeremo la crittografia a chiave pubblica basata su Ring-LWE (Learning With Errors su anelli),
una costruzione comune in crittografia moderna.
Obiettivo del Progetto
Generazione delle chiavi: Creare una chiave pubblica e una chiave privata utilizzando un anello locale.
Cifratura di un messaggio: Utilizzare la chiave pubblica per cifrare un messaggio.

Decifratura del messaggio: Utilizzare la chiave privata per decifrare il messaggio cifrato.
'''
import numpy as np
import sympy as sp

def generate_keys(n, q):
    # Genera un polinomio irriducibile per modulo q
    x = sp.symbols('x')
    f = sp.primitive_root(q)
    f_poly = sp.Poly(f**n + 1, x, modulus=q)
    
    # Genera la chiave privata s e la chiave pubblica a
    s = np.random.randint(0, q, n)
    a = np.random.randint(0, q, n)
    
    # Calcola la chiave pubblica b = a * s + e (dove e è l'errore)
    e = np.random.randint(-1, 2, n)  # errore piccolo
    b = (a * s + e) % q
    
    return (a, b), s

def encrypt(public_key, message, q):
    a, b = public_key
    n = len(a)
    
    # Rappresenta il messaggio come un polinomio
    m = np.array([int(bit) for bit in format(message, f'0{n}b')])
    
    # Genera il polinomio di errore
    e1 = np.random.randint(-1, 2, n)
    e2 = np.random.randint(-1, 2, n)
    
    # Calcola il cifrato
    u = (a * e1) % q
    v = (b * e1 + e2 + m) % q
    
    return u, v

def decrypt(private_key, ciphertext, q):
    s = private_key
    u, v = ciphertext
    n = len(s)
    
    # Decifra il messaggio
    m = (v - u * s) % q
    
    # Converti il messaggio dal polinomio a un numero
    message = 0
    for i in range(n):
        message += m[i] * (2 ** (n - 1 - i))
    
    return message

# Parametri
n = 8  # dimensione del polinomio
q = 257  # modulo (numero primo)

# Generazione delle chiavi
public_key, private_key = generate_keys(n, q)
print("Chiave Pubblica:", public_key)
print("Chiave Privata:", private_key)

# Messaggio da cifrare (es. 42)
message = 42
print("Messaggio Originale:", message)

# Cifratura
ciphertext = encrypt(public_key, message, q)
print("Messaggio Cifrato:", ciphertext)

# Decifratura
decrypted_message = decrypt(private_key, ciphertext, q)
print("Messaggio Decifrato:", decrypted_message)
