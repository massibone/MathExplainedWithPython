'''
determinare tutti e soli i valori di x in cui l'uguaglianza insiemistica {x, x - 1} = {0, 1} è vera,
dobbiamo confrontare gli elementi di entrambi gli insiemi e vedere quando sono uguali. In altre parole, cerchiamo i valori di x per cui:

x è uguale a 0 o x è uguale a 1 (perché 0 e 1 sono gli elementi dell'insieme {0, 1}).
x - 1 è uguale a 0 o x - 1 è uguale a 1 (perché 0 e 1 sono gli elementi dell'insieme {0, 1}).
Ora risolviamo entrambe queste condizioni:

x = 0 oppure x = 1
x - 1 = 0 oppure x - 1 = 1
Per la prima condizione, x deve essere uguale a 0 o 1. Per la seconda condizione, x deve essere uguale a 1 o 2.

Ora, mettendo insieme entrambe le condizioni, vediamo quali sono i valori di x che soddisfano entrambe le condizioni:

x deve essere uguale a 1.

Quindi, tutti e soli i valori di x in cui l'uguaglianza insiemistica {x, x - 1} = {0, 1} è vera sono x = 1.



'''

# Inizializza un insieme vuoto per contenere i valori di x
soluzioni_x = set()

# Definisci l'insieme di confronto {0, 1}
insieme_confronto = {0, 1}

# Itera su tutti i possibili valori di x in un intervallo che ritieni opportuno
for x in range(-100, 101):  # Esempio: considera x da -100 a 100
    # Crea l'insieme {x, x - 1} per il valore corrente di x
    insieme_x = {x, x - 1}
    
    # Confronta l'insieme appena creato con l'insieme di confronto {0, 1}
    if insieme_x == insieme_confronto:
        soluzioni_x.add(x)

# Stampa i valori di x che soddisfano l'uguaglianza insiemistica
print("Valori di x che soddisfano l'uguaglianza insiemistica:", soluzioni_x)
