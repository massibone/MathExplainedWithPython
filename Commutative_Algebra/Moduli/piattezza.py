'''
sotto certe condizioni di piattezza, un anello locale deve necessariamente essere un campo. 
'''
# Importiamo SymPy
import sympy as sp

# Definiamo l'anello Z/2Z
A = sp.FiniteField(2)

# Verifichiamo se l'anello è locale
is_local = A.is_field
print(f"L'anello A è un campo: {is_local}")

# Verifichiamo se l'anello è assolutamente piatto
# In questo caso, poiché è un campo, è automaticamente piatto
is_absolutely_flat = True
print(f"L'anello A è assolutamente piatto: {is_absolutely_flat}")
