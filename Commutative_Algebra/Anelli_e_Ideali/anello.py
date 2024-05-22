class Anello:
    def __init__(self, insieme_elementi, operazione_addizione, operazione_moltiplicazione):
        self.insieme_elementi = insieme_elementi
        self.operazione_addizione = operazione_addizione
        self.operazione_moltiplicazione = operazione_moltiplicazione

    def somma(self, elemento1, elemento2):
        return self.operazione_addizione(elemento1, elemento2)

    def prodotto(self, elemento1, elemento2):
        return self.operazione_moltiplicazione(elemento1, elemento2)

# Definizione di un insieme di elementi e delle operazioni di addizione e moltiplicazione
insieme_interi = set(range(-10, 11))
def addizione_interi(a, b):
    return a + b
def moltiplicazione_interi(a, b):
    return a * b

# Creazione di un'istanza della classe Anello per gli interi con le operazioni di addizione e moltiplicazione definite
anello_interi = Anello(insieme_interi, addizione_interi, moltiplicazione_interi)

