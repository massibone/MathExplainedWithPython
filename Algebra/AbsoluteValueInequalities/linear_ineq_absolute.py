

# |2x-3|>x+6
# 2x-3>=0           2x-3<0
# 2x-3> x+6         -2x+3> x+6

from sympy import *
init_printing()

x = Symbol('x')
eq1=(2*x-3)>=0
eq2=(2*x-3)>x+6

eq3=(2*x-3)<0
eq4=(-2*x+3)>x+6

sistem1=(solve([eq1,eq2]))
sistem2=(solve([eq3,eq4]))

print(sistem1,sistem2)
