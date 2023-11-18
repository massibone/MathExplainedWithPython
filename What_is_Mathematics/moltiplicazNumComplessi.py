
def moltiplica_complessi(z1, z2):
    # Estrarre parte reale e parte immaginaria dai numeri complessi
    parte_reale_z1, parte_immaginaria_z1 = z1
    parte_reale_z2, parte_immaginaria_z2 = z2
    
    # Calcolare la parte reale della moltiplicazione
    parte_reale_risultato = (parte_reale_z1 * parte_reale_z2) - (parte_immaginaria_z1 * parte_immaginaria_z2)
    
    # Calcolare la parte immaginaria della moltiplicazione
    parte_immaginaria_risultato = (parte_reale_z1 * parte_immaginaria_z2) + (parte_immaginaria_z1 * parte_reale_z2)
    
    # Restituire il risultato come un numero complesso
    return (parte_reale_risultato, parte_immaginaria_risultato)

# Numeri complessi in forma (parte reale, parte immaginaria)
z1 = (2, 3)  # 2 + 3i
z2 = (1, -1)  # 1 - i

# Calcolare il risultato della moltiplicazione dei numeri complessi
risultato_moltiplicazione = moltiplica_complessi(z1, z2)

# Stampare il risultato
print("Il risultato della moltiplicazione è:", f"{risultato_moltiplicazione[0]} + {risultato_moltiplicazione[1]}i")
