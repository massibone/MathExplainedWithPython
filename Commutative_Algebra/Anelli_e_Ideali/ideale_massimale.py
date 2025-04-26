# Definizione di un insieme di numeri 
# interi che costituiscono l'anello
numeri_interi = {0, 1, 2, 3, 4, 5}

# Definizione degli ideali massimali (insieme di numeri primi)
ideali_massimali = {2, 3, 5}

# Verifica se un numero è in un ideale massimale
def in_ideale_massimale(numero):
    return numero in ideali_massimali

# Esempio di utilizzo
numero_da_verificare = 3
if in_ideale_massimale(numero_da_verificare):
    print(f"Il numero {numero_da_verificare} è in un ideale massimale.")
else:
    print(f"Il numero {numero_da_verificare} non è in un ideale massimale.")

creare cartella Moduli/readme
l'algebra commutativa moderna dà maggiore importanza ai moduli, piuttosto che agli ideali.
