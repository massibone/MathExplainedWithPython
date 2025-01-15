def generatore_progressivo():
    numero = 10
    def get_prossimo_numero():
        nonlocal numero
        numero += 1
        return numero
    return get_prossimo_numero

generatore = generatore_progressivo()
print(generatore())  # 11
print(generatore())  # 12
