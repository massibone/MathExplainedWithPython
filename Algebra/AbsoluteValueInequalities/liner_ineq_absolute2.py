# |x^2-5|< 4
# x^2 -5 >= 0          x^2 -5 < 0
# x^2 -5 < 4          -x^2+5 < 4

from sympy import *
init_printing()

x = Symbol('x')
eq1=(x**2-5)>=0
eq2=(x**2-5)< 4

eq3=(x**2-5)<0
eq4=(-x**2+5)<4

sistem1=(solve([eq1,eq2]))
sistem2=(solve([eq3,eq4]))

print(sistem1,sistem2)
