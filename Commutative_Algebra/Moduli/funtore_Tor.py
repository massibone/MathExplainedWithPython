'''
Il funtore Tor è uno strumento potente in algebra omologica e teoria dei moduli. È utilizzato per misurare quanto una sequenza esatta di moduli fallisce nel rimanere esatta dopo aver applicato il prodotto tensoriale. In altre parole, il funtore Tor aiuta a capire le relazioni tra moduli e la loro struttura.
Esempio Intuitivo
Immagina di avere una catena di anelli metallici collegati tra loro, e vuoi vedere cosa succede se applichi una forza a questa catena. Se la catena si spezza in certi punti, il funtore Tor misura esattamente dove e come si spezza.

In termini di moduli, immagina di avere una sequenza di moduli (insiemi strutturati di numeri o vettori) e vuoi vedere cosa succede se combini questi moduli con un altro modulo usando il prodotto tensoriale. Se la combinazione non si comporta come ti aspetti, il funtore Tor ti dice dove sta il problema.
'''

import sympy as sp

# Definizione degli anelli e dei moduli
Z = sp.ZZ  # Anello degli interi
m = 4
n = 3
ZmZ = Z.quo(m)  # Anello degli interi modulo m
ZnZ = Z.quo(n)  # Anello degli interi modulo n

# Calcolo del modulo tensore (Z/mZ) ⊗Z (Z/nZ)
tensor_module = sp.tensor_product(ZmZ, ZnZ)

# Funzione per calcolare Tor_1(Z/mZ, Z/nZ)
def tor_1_z_mod_m_n(m, n):
    gcd = sp.gcd(m, n)
    if gcd != 1:
        return sp.ZZ.quo(gcd)  # Tor_1 è Z/gcd(m, n)Z se m e n non sono coprimi
    return sp.Zero  # Tor_1 è 0 se m e n sono coprimi

# Calcolo di Tor_1(Z/mZ, Z/nZ)
tor_1 = tor_1_z_mod_m_n(m, n)

# Stampiamo i risultati
print(f"Il modulo tensore (Z/{m}Z) ⊗Z (Z/{n}Z) è: {tensor_module}")
print(f"Il funtore Tor_1(Z/{m}Z, Z/{n}Z) è: {tor_1}")
