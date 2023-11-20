'''
Passi metodo di induzione
'''
from fractions import Fraction

def base_of_induction():
    print("Base dell'induzione (n = 1):")
    lhs = Fraction(1, 2)
    rhs = Fraction(2, 1) - Fraction(1 + 2, 4)
    print(f"LHS = {lhs}")
    print(f"RHS = {rhs}")
    if lhs == rhs:
        print("L'uguaglianza è verificata per n = 1.\n")
    else:
        print("L'uguaglianza non è verificata per n = 1.\n")

def step_of_induction(n):
    lhs = sum(Fraction(i, 2 ** i) for i in range(1, n+1))
    rhs = Fraction(2) - Fraction(n + 2, 2 ** (n + 1))

    print(f"Passo induttivo (n = {n}):")
    print(f"LHS = {lhs}")
    print(f"RHS = {rhs}")
    if lhs == rhs:
        print(f"L'uguaglianza è verificata per n = {n}.\n")
    else:
        print(f"L'uguaglianza non è verificata per n = {n}.\n")

# Esegui la dimostrazione per n = 1, 2, 3, 4 (puoi cambiare il range)
for n in range(1, 5):
    base_of_induction()
    for i in range(1, n+1):
        step_of_induction(i)
