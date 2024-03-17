
'''
La legge di Hooke descrive il comportamento di un materiale elastico sotto l'azione di una forza. In breve, essa stabilisce che lo spostamento (deformazione) di un materiale elastico è direttamente proporzionale alla forza applicata su di esso.
'''
class MaterialeElastico:
    def __init__(self, k):
        self.k = k  # Costante elastica del materiale

    def spostamento(self, forza):
        # Calcolo dello spostamento utilizzando la legge di Hooke: F = k * x
        spostamento = forza / self.k
        return spostamento

# Esempio di utilizzo della classe MaterialeElastico
if __name__ == "__main__":
    # Creazione di un materiale elastico con una costante elastica di 2 N/m
    materiale = MaterialeElastico(k=2)

    # Forza applicata di 5 N
    forza_applicata = 5

    # Calcolo dello spostamento utilizzando la legge di Hooke
    spostamento = materiale.spostamento(forza_applicata)
    print("Lo spostamento del materiale elastico sotto una forza di", forza_applicata, "N è:", spostamento, "m")
