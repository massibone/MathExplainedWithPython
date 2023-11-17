def modulo_6(n):
    return n % 6

# Creazione delle liste per le operazioni
somme_mod_6 = [modulo_6(i + j) for i in range(500) for j in range(500)]
sottrazioni_mod_6 = [modulo_6(i - j) for i in range(500) for j in range(1, 500)]
moltiplicazioni_mod_6 = [modulo_6(i * j) for i in range(500) for j in range(500)]
divisioni_mod_6 = [modulo_6(i // j) for i in range(1, 500) for j in range(1, 500) if j != 0]

# Rimuovi duplicati e ordina le liste
somme_mod_6 = sorted(list(set(somme_mod_6)))
sottrazioni_mod_6 = sorted(list(set(sottrazioni_mod_6)))
moltiplicazioni_mod_6 = sorted(list(set(moltiplicazioni_mod_6)))
divisioni_mod_6 = sorted(list(set(divisioni_mod_6)))

# Stampa le liste
print("Interi modulo 6 ottenuti tramite somma:", somme_mod_6)
print("\nInteri modulo 6 ottenuti tramite sottrazione:", sottrazioni_mod_6)
print("\nInteri modulo 6 ottenuti tramite moltiplicazione:", moltiplicazioni_mod_6)
print("\nInteri modulo 6 ottenuti tramite divisione:", divisioni_mod_6)
