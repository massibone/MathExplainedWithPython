import sympy as sp

x = sp.symbols('x')
equation_a = x**4 - 4*x**2 + 1

solutions_a = sp.solve(equation_a, x)
print("Solutions for x = sqrt(2 + sqrt(3)):")
print(solutions_a)

equation_b = x**4 - 10*x**2 + 1

solutions_b = sp.solve(equation_b, x)
print("\nSolutions for x = sqrt(2) + sqrt(3):")
print(solutions_b)

equation_c = 484*x**4 - 220*x**2 + 22 - 3

solutions_c = sp.solve(equation_c, x)
print("\nSolutions for x = 1/sqrt(5 + sqrt(3)):")
print(solutions_c)
