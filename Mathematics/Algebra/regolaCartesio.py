'''
La regola dei segni di Cartesio è un metodo utilizzato per determinare il numero di radici positive e negative di un polinomio a coefficienti reali contando le variazioni dei segni dei coefficienti. 
'''
def cartesio_rule(coefficients):
    sign_changes = 0
    for i in range(len(coefficients) - 1):
        if coefficients[i] * coefficients[i + 1] < 0:
            sign_changes += 1
    return sign_changes

# Esempio di utilizzo
coefficients = [1, -2, -3, 4]  # Coefficienti del polinomio: x^3 - 2x^2 - 3x + 4
number_of_positive_roots = cartesio_rule(coefficients)
number_of_negative_roots = cartesio_rule(coefficients[::-1])  # Inverti i coefficienti per trovare le radici negative

print("Numero di radici positive:", number_of_positive_roots)
print("Numero di radici negative:", number_of_negative_roots)
