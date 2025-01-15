def cache():
    cache = {}
    def get_valore(key):
        nonlocal cache
        if key in cache:
            return cache[key]
        else:
            valore = get_valore_reale(key)
            cache[key] = valore
            return valore
    def get_valore_reale(key):
        # codice per ottenere il valore reale
        return key * 2
    return get_valore

cache = cache()
print(cache(10))  # 20
print(cache(20))  # 40
