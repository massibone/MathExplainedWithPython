'''
Useremo un anello di Dedekind astratto e illustreremo la localizzazione
'''
import sympy as sp
from sympy.abc import x

# Definiamo un dominio di Dedekind astratto
# In questo esempio usiamo il dominio degli interi algebrici in Q(sqrt(-5))
A = sp.QQ.algebraic_field(x**2 + 5)

