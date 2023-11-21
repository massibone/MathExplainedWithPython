'''
Es devo scrivere 144= 2^4 * 3^2
col metodo dei divisori
'''

def scomposizione_fattori_primi(numero):
    fattori_primi = []
    esponenti = []

    # Trova i fattori primi 2
    while numero % 2 == 0:
        fattori_primi.append(2)
        esponenti.append(1)
        numero //= 2

    # Trova i fattori primi maggiori di 2
    for i in range(3, int(numero ** 0.5) + 1, 2):
        while numero % i == 0:
            fattori_primi.append(i)
            esponenti.append(1)
            numero //= i

    # Se il numero residuo è maggiore di 2, è un fattore primo
    if numero > 2:
        fattori_primi.append(numero)
        esponenti.append(1)

    return fattori_primi, esponenti


def rappresenta_prodotto_potenze(fattori_primi, esponenti):
    rappresentazione = ""
    for i in range(len(fattori_primi)):
        rappresentazione += str(fattori_primi[i])
        if esponenti[i] > 1:
            rappresentazione += f"^{esponenti[i]}"
        if i < len(fattori_primi) - 1:
            rappresentazione += " * "

    return rappresentazione


# Esempio di utilizzo per il numero 144
numero_da_scomporre = 144
fattori_primi, esponenti = scomposizione_fattori_primi(numero_da_scomporre)
rappresentazione = rappresenta_prodotto_potenze(fattori_primi, esponenti)

print(f"Scomposizione in fattori primi di {numero_da_scomporre}:")
print(f"Fattori primi: {fattori_primi}")
print(f"Esponenti: {esponenti}")
print(f"Rappresentazione come prodotto di potenze: {rappresentazione}")
