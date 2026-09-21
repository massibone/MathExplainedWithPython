from sympy import plot_implicit, Eq
from sympy.abc import x, y

a = -1
b = 3
plot_implicit(Eq((y - a * x) * (y - b * x), -1), (x, -10, 10), (y, -10, 10))

