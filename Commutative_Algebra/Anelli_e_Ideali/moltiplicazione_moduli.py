'''
se nella scatola "Modulo 5" hai i numeri 1 e 3, e nella scatola "Modulo 3" hai i numeri 0 e 2, allora il prodotto di questi due sottomoduli sarebbe:

1 * 0 = 0 (nel Modulo 5, 0 resta 0)
1 * 2 = 2 (nel Modulo 5, 2 resta 2)
3 * 0 = 0 (nel Modulo 5, 0 resta 0)
3 * 2 = 1 (nel Modulo 5, 6 diventa 1)
Quindi, il prodotto di questi due sottomoduli sarebbe una nuova scatola con gli elementi 0, 1 e 2, nel Modulo 5
'''
def modulo_multiplication(modulo1, modulo2):
    result = set()
    for num1 in modulo1:
        for num2 in modulo2:
            # Calcola il prodotto dei due numeri nei rispettivi moduli
            product = (num1 * num2) % max(len(modulo1), len(modulo2))
            result.add(product)
    return result
  
# Esempio di sottomoduli
modulo_5 = {0, 1, 2, 3, 4}
modulo_3 = {0, 1, 2}

# Calcola il prodotto dei due sottomoduli
product_result = modulo_multiplication(modulo_5, modulo_3)
print("Il prodotto dei due sottomoduli è:", product_result)
