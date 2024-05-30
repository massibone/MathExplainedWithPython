# Funzione per trovare i divisori dello zero in un anello
def zero_divisors(ring_elements):
    zero_divs = []
    for elem in ring_elements:
        if elem != 0:
            for other_elem in ring_elements:
                if elem * other_elem == 0:
                    zero_divs.append(elem)
                    break
    return zero_divs

# Funzione per individuare gli elementi nilpotenti in un anello
def nilpotent_elements(ring_elements):
    nilpotents = []
    for elem in ring_elements:
        if elem ** 2 == 0:  # Verifica se l'elemento elevato al quadrato è zero
            nilpotents.append(elem)
    return nilpotents

# Funzione per trovare gli elementi invertibili in un anello
def invertible_elements(ring_elements):
    invertibles = []
    for elem in ring_elements:
        if elem != 0:  # Assicura che l'elemento non sia lo zero
            for other_elem in ring_elements:
                if elem * other_elem == 1:  # Verifica se esiste un inverso moltiplicativo
                    invertibles.append(elem)
                    break
    return invertibles

# Esempio di utilizzo delle funzioni con un insieme di elementi di un anello
ring_elements = [0, 1, 2, 3, 4, -1, -2]
print("Divisori dello Zero:", zero_divisors(ring_elements))
print("Elementi Nilpotenti:", nilpotent_elements(ring_elements))
print("Elementi Invertibili:", invertible_elements(ring_elements))
