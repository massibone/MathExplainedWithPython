'''
La regola del parallelogramma è una rappresentazione geometrica utilizzata per l'addizione di numeri complessi. Essa mostra come sommare due numeri complessi utilizzando il concetto di vettori in un piano complesso.
'''
def somma_complessi(z1, z2):
    # Estrarre parte reale e parte immaginaria dai numeri complessi
    parte_reale_z1, parte_immaginaria_z1 = z1
    parte_reale_z2, parte_immaginaria_z2 = z2
  
  # Calcolare la somma delle parti reali e delle parti immaginarie
    somma_reale = parte_reale_z1 + parte_reale_z2
    somma_immaginaria = parte_immaginaria_z1 + parte_immaginaria_z2
    
    # Restituire la somma come un numero complesso
    return (somma_reale, somma_immaginaria)

# Numeri complessi in forma (parte reale, parte immaginaria)
z1 = (2, 3)  # 2 + 3i
z2 = (1, -1)  # 1 - i

# Calcolare la somma dei numeri complessi
risultato = somma_complessi(z1, z2)

# Stampare il risultato
print("La somma dei numeri complessi è:", f"{risultato[0]} + {risultato[1]}i")
