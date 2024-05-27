'''
In questo codice:

Viene generata una coppia di chiavi RSA.
Viene creato un messaggio di testo da cifrare.
Il messaggio viene cifrato utilizzando la chiave pubblica.
Il messaggio cifrato viene quindi decifrato utilizzando la chiave privata.
'''
# crittografiaAsimmetrica.py

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

# Generazione della coppia di chiavi RSA
def generate_rsa_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key

# Cifrare il messaggio con la chiave pubblica
def encrypt_message(public_key, message):
    encrypted_message = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_message

# Decifrare il messaggio con la chiave privata
def decrypt_message(private_key, encrypted_message):
    decrypted_message = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_message

# Funzione principale
def main():
    # Generazione delle chiavi
    private_key, public_key = generate_rsa_keys()
    
    # Messaggio da cifrare
    message = b'Questo è un messaggio segreto.'
    
    # Cifratura del messaggio
    encrypted_message = encrypt_message(public_key, message)
    print("Messaggio cifrato:", encrypted_message)
    
    # Decifratura del messaggio
    decrypted_message = decrypt_message(private_key, encrypted_message)
    print("Messaggio decifrato:", decrypted_message.decode('utf-8'))

if __name__ == "__main__":
    main()
