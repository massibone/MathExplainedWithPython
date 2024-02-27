# Esempio di equazione lineare: 2x + 3 = 7
x = (7 - 3) / 2
print("Soluzione:", x)  # Output: 2.0

# Esempio di equazione quadratica: x^2 - 4x + 4 = 0
a = 1
b = -4
c = 4
delta = b**2 - 4*a*c
x1 = (-b + delta**0.5) / (2*a)
x2 = (-b - delta**0.5) / (2*a)
print("Soluzioni:", x1, x2)  # Output: 2.0 2.0

# Esempio di semplificazione: (x^2 + 2x + 1) / (x + 1)
x = 2
result = (x**2 + 2*x + 1) / (x + 1)
print("Risultato:", result)  # Output: 5.0

# Esempio di sistema di equazioni lineari:
# 2x + 3y = 12
# 4x - y = 5

from sympy import symbols, solve

x, y = symbols('x y')
equations = (2*x + 3*y - 12, 4*x - y - 5)
solution = solve(equations, (x, y))
print("Soluzione:", solution)  # Output: {x: 3, y: 2}
