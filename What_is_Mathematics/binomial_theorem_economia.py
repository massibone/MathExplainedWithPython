import math

def binomial_coefficient(n, k):
    """Calcola il coefficiente binomiale C(n, k)"""
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def calculate_probability(n, k, p_up, p_down):
    """Calcola la probabilità di raggiungere k aumenti in n periodi"""
    return binomial_coefficient(n, k) * (p_up ** k) * (p_down ** (n - k))

def calculate_option_price(S, K, r, T, u, d, n):
    """Calcola il prezzo di un'opzione call europea utilizzando il modello di binomio"""
    p_up = (1 + r) * u  # Probabilità di aumento
    p_down = (1 + r) * d  # Probabilità di diminuzione

    option_price = 0
    for k in range(n + 1):
        option_price += calculate_probability(n, k, p_up, p_down) * max(0, S * (p_up ** k) * (p_down ** (n - k)) - K)

    option_price /= (1 + r) ** n  # Discounting

    return option_price

# Parametri
S = 50  # Prezzo iniziale dell'azione
K = 60  # Prezzo di esercizio dell'opzione
r = 0.05  # Tasso di interesse senza rischio
T = 3  # Numero di periodi
u = 0.10  # Aumento percentuale del prezzo dell'azione in un periodo
d = -0.10  # Diminuzione percentuale del prezzo dell'azione in un periodo
n = T  # Numero di periodi nel modello di binomio

# Calcolo del prezzo dell'opzione call
option_price = calculate_option_price(S, K, r, T, u, d, n)

# Calcolo della probabilità di raggiungere il prezzo K
k = n  # Tutti gli aumenti
probability = calculate_probability(n, k, (1 + r) * u, (1 + r) * d)

# Risultati
print(f"Prezzo dell'opzione call: {option_price:.2f}")
print(f"Probabilità di raggiungere il prezzo di esercizio: {probability:.2%}")
