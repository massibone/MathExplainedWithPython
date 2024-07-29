'''
Per pianificare operazioni periodiche in un sistema distribuito con diverse macchine o processi che operano a intervalli differenti, puoi utilizzare il Teorema Cinese dei Resti per sincronizzare i tempi di esecuzione. Questo può essere utile in scenari come il bilanciamento del carico, la sincronizzazione dei backup, o l'esecuzione di compiti periodici in un cluster eterogeneo.

Step 1: Definire i Periodi delle Operazioni
Prima di tutto, definisci i periodi di esecuzione delle operazioni su ciascuna macchina. Ad esempio:

Macchina Windows: 15 secondi
Macchina Linux: 20 secondi
Step 2: Calcolare il Tempo di Sincronizzazione
Utilizzeremo il Teorema Cinese dei Resti per calcolare il tempo minimo 
𝑡 dopo il quale tutte le operazioni saranno sincronizzate.
'''
from sympy.ntheory.modular import crt

# Definizione dei periodi
windows_period = 15
linux_period = 20

# Definizione dei moduli e dei residui
n = [windows_period, linux_period]
a = [0, 0]

# Utilizzo del Teorema Cinese dei Resti
t, _ = crt(n, a)

print(f"Le operazioni saranno sincronizzate ogni {t} secondi.")
