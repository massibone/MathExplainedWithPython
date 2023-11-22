'''
Per calcolare le approssimazioni al decimillesimo (10^(-5)) delle radici cubiche di 2 e 5, possiamo utilizzare il metodo della bisezione, noto anche come metodo di Newton-Raphson
'''

def bisection_cubic_root(target, epsilon):
    # Intervallo iniziale [a, b]
    a = 0.0
    b = target

    # Calcolo approssimazione
    while abs(b - a) > epsilon:
        mid = (a + b) / 2
        mid_cubed = mid ** 3

        if mid_cubed > target:
            b = mid
        else:
            a = mid

    return (a + b) / 2

# Calcola radice cubica di 2 con precisione 10^(-5)
approx_cubic_root_2 = bisection_cubic_root(2, 1e-5)
print("Radice cubica di 2:", approx_cubic_root_2)

# Calcola radice cubica di 5 con precisione 10^(-5)
approx_cubic_root_5 = bisection_cubic_root(5, 1e-5)
print("Radice cubica di 5:", approx_cubic_root_5)


from fractions import Fraction

# Calcola la radice cubica di 2 come frazione
cubic_root_2 = Fraction(2) ** Fraction(1, 3)
print("Radice cubica di 2 come frazione:", cubic_root_2)

# Calcola la radice cubica di 5 come frazione
cubic_root_5 = Fraction(5) ** Fraction(1, 3)
print("Radice cubica di 5 come frazione:", cubic_root_5)
