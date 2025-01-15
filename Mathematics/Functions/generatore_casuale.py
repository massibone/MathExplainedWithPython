import random

def generatore_casuale():
    seed = 10
    def get_numero_casuale():
        nonlocal seed
        seed = random.randint(0, 100)
        return seed
    return get_numero_casuale

generatore = generatore_casuale()
print(generatore())  # 42
print(generatore())  # 13
