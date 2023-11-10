import string

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Trova un esponente di crittografia e
    e = 65537  # Scelto comunemente come esponente
    while gcd(e, phi) != 1:
        e += 2
    
    # Trova un esponente di decrittografia d
    d = mod_inverse(e, phi)
    
    return ((e, n), (d, n))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def encrypt(text, public_key):
    e, n = public_key
    encrypted_text = [pow(ord(char), e, n) for char in text]
    return encrypted_text

def decrypt(encrypted_text, private_key):
    d, n = private_key
    decrypted_text = [chr(pow(char, d, n)) for char in encrypted_text]
    return ''.join(decrypted_text)

# Esempio numerico
p = 61
q = 53
public_key, private_key = generate_keypair(p, q)

# Messaggio da cifrare
message = "Hello, RSA!"
print("Messaggio originale:", message)

# Cifratura
encrypted_message = encrypt(message, public_key)
print("Messaggio cifrato:", encrypted_message)

# Decifratura
decrypted_message = decrypt(encrypted_message, private_key)
print("Messaggio decifrato:", decrypted_message)
