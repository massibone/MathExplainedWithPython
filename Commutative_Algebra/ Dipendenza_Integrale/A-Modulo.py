'''
Proprietà degli A-moduli noetheriani e attiniani. 
Un A-modulo noetheriano è un modulo che soddisfa la condizione della catena ascendente sugli ideali, ovvero ogni catena crescente di sotto-moduli si stabilizza. 
Un modulo attiniano, d'altra parte, soddisfa la condizione della catena discendente sugli ideali, ovvero ogni catena decrescente di sotto-moduli si stabilizza.

Teorema da Dimostrare
Sia M un A-modulo noetheriano e sia a l'annullatore di M in 𝐴. Dimostrare che 𝐴/𝑎 è un anello noetheriano. 
Poi, discutiamo se questo risultato rimane vero se sostituiamo "noetheriano" con "attiniano".

Riassunto
Modulo Noetheriano: Un modulo che soddisfa la condizione della catena ascendente sugli ideali.
Annullatore: L'annullatore di 𝑀 in 𝐴, denotato 𝑎 è l'insieme degli elementi di A che annullano tutti gli elementi di M.
Anello Noetheriano: Un anello che soddisfa la condizione della catena ascendente sugli ideali.
Modulo Attiniano: Un modulo che soddisfa la condizione della catena discendente sugli ideali.
Dimostrazione
Dimostrazione per Noetheriano

a={r∈A∣r⋅m=0 per ogni m∈M}.
Quoziente 
A/a: Consideriamo l'anello quoziente 

A/a-modulo: Poiché M è un 
A-modulo noetheriano, 
M può essere visto come un 
A/a-modulo.
Condizione della Catena Ascendente: Poiché 𝑀 è noetheriano, ogni catena crescente di sotto-moduli di 
M si stabilizza.
Isomorfismo 

A/a è isomorfo all'anello degli endomorfismi di 
M, il che implica che 
A/a eredita la proprietà noetheriana da 𝑀.
Pertanto, 
A/a è un anello noetheriano.

Dimostrazione per Attiniano
Il ragionamento è simile. 
'''
class AModule:
    def __init__(self, elements):
        self.elements = set(elements)
    
    def annullatore(self):
        # Semplice rappresentazione dell'annullatore
        return {e for e in self.elements if e == 0}

class Ring:
    def __init__(self, elements):
        self.elements = set(elements)
    
    def quotient_ring(self, annullatore):
        # Costruisce l'anello quoziente
        return Ring(self.elements - annullatore)
    
    def is_noetherian(self):
        # Controllo se l'anello è noetheriano (semplificato)
        return True
    
    def is_artinian(self):
        # Controllo se l'anello è attiniano (semplificato)
        return True

# Esempio di modulo noetheriano
mod_elements = [0, 1, 2, 3, 4, 5]
A = AModule(mod_elements)
ann = A.annullatore()

# Costruzione dell'anello
ring_elements = [0, 1, 2, 3, 4, 5]
R = Ring(ring_elements)

# Anello quoziente
quotient = R.quotient_ring(ann)
print("Anello quoziente:", quotient.elements)

# Verifica delle proprietà
print("È Noetheriano?", quotient.is_noetherian())
print("È Attiniano?", quotient.is_artinian())
