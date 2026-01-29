# Zero-Theorem

The Rational Zeros Theorem states: 
If P(x) is a polynomial with integer coefficients and if is a zero of P(x) (P( ) = 0), 
then p is a factor of the constant term of P(x) and q is a factor of the leading coefficient of P(x). 
We can use the Rational Zeros Theorem to find all the rational zeros of a polynomial.

from zero_theorem import possible_rational_zeros, test_rational_zeros, poly_eval

# Esempio: P(x) = 2x^3 + 3x^2 - 5x + 1 (coeff: [2, 3, -5, 1])
coeffs = [2, 3, -5, 1]
candidates = possible_rational_zeros(coeffs)
print("Possibili zeri:", candidates)  # ±1, ±1/2

zeros = test_rational_zeros(coeffs, candidates)
print("Zeri razionali trovati:", zeros)  # Es. [1/2] se presente

Output esempio:

Possibili zeri: [Fraction(1, 1), Fraction(-1, 1), Fraction(1, 2), Fraction(-1, 2)]
Zeri razionali trovati: [Fraction(1, 2)]

Polinomio Cubico

coeffs = [3, -2, -8, 4]  # 3x^3 - 2x^2 -8x +4
# Possibili: ±1,2,4,1/3,2/3,4/3

Con NumPy (confronto)

import numpy as np
roots_all = np.roots(coeffs)  # Tutte le roots (complesse)
print(roots_all)
