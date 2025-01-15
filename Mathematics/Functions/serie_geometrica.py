def serie_geometrica():
    a = 2
    r = 3
    def get_somma(n):
        nonlocal a, r
        somma = 0
        for i in range(n):
            somma += a * (r ** i)
        return somma
    return get_somma

serie = serie_geometrica()
print(serie(5))  # 242
print(serie(10))  # 6404
