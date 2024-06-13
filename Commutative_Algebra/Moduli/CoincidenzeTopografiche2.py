'''
L'Anello e le Topologie
Immagina che un anello sia come un negozio di giocattoli. In questo negozio ci sono tanti tipi di giocattoli che rappresentano gli elementi dell'anello. Alcuni di questi giocattoli sono speciali e possono essere combinati in modi particolari, rappresentando le regole matematiche dell'anello.

La Topologia di Zariski
Pensa alla topologia di Zariski come un modo di organizzare i giocattoli sugli scaffali del negozio. Immagina che alcuni scaffali siano considerati "chiusi" e altri "aperti". Questi scaffali possono essere etichettati con regole specifiche su come i giocattoli devono essere disposti.

La Topologia Costruibile
La topologia costruibile è un altro modo di organizzare i giocattoli, dove possiamo avere combinazioni più complesse, come mescolare un po' di scaffali chiusi con alcuni aperti per creare nuovi scaffali. Questi nuovi scaffali devono seguire anche delle regole.

Nilradicale
Immagina che nel negozio ci siano alcuni giocattoli difettosi che non funzionano bene. Questi giocattoli difettosi sono come il nilradicale. Quando togliamo tutti i giocattoli difettosi dal negozio, otteniamo un negozio più semplice e pulito, che rappresenta l'anello 
A/R, dove 𝑅 è il nilradicale.

Assolutamente Piatto
Immagina che un modo di organizzare i giocattoli sugli scaffali sia molto buono e funziona perfettamente in ogni situazione. Questo è ciò che intendiamo con assolutamente piatto. Significa che il negozio (o l'anello 
A/R) è organizzato in un modo così efficiente che tutte le combinazioni di scaffali funzionano bene insieme.

Coincidenza delle Topologie
Ora, vogliamo sapere quando la topologia di Zariski e la topologia costruibile sono essenzialmente la stessa cosa. Questo succede se e solo se il negozio senza i giocattoli difettosi (A/R) è organizzato in modo perfetto e funzionante (assolutamente piatto).
'''
# Simuliamo un negozio di giocattoli con due tipi di organizzazione

class ToyStore:
    def __init__(self, toys):
        self.toys = toys

# Controlla se un'organizzazione è assolutamente perfetta (assolutamente piatta)
def is_absolutely_flat(store):
    # Simuliamo che il negozio è perfetto se ha più di 3 tipi di giocattoli
    return len(store.toys) > 3

# Funzione principale per verificare la coincidenza delle topologie
def check_topologies():
    # Creiamo un negozio di giocattoli con alcuni giocattoli
    original_store = ToyStore(["car", "doll", "ball", "puzzle"])
    
    # Rimuoviamo i giocattoli difettosi (nilradicale)
    cleaned_store = ToyStore(["car", "doll", "ball"])

    # Verifichiamo se il negozio pulito è organizzato perfettamente
    if is_absolutely_flat(cleaned_store):
        print("Le due organizzazioni coincidono!")
    else:
        print("Le due organizzazioni non coincidono!")

# Eseguiamo la funzione principale
check_topologies()
