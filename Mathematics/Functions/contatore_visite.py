def contatore_visite():
    contatore = 0
    def incrementa_visita():
        nonlocal contatore
        contatore += 1
        return contatore
    return incrementa_visita

contatore = contatore_visite()
print(contatore())  # 1
print(contatore())  # 2
