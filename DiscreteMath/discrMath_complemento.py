'''
Siano A e B due insiemi generici contenuti in un insieme universo X (con A, B, X
non vuoti). Quale è la soluzione?
"(A ∪ B) ∩ ∅" è l'intersezione tra l'unione di A e B e l'insieme vuoto (∅). Analizziamo cosa significa questa espressione:

A e B sono due insiemi generici contenuti in un insieme universo X, quindi fanno parte di XX.

∅ (insieme vuoto) è un insieme che non contiene alcun elemento.

L'intersezione tra A ∪ B e t∅ (A ∪ B ∩ ∅)rappresenta l'insieme che contiene gli elementi che sono contemporaneamente presenti in A ∪ B e in ∅. Tuttavia, l'insieme vuoto non contiene alcun elemento, quindi questa intersezione sarà vuota, ovvero (A∪B)∩∅=∅.
Quindi, l'equazione "(A ∪ B) ∩ ∅ = ∅" significa che l'intersezione tra l'unione di A e B e l'insieme vuoto è l'insieme vuoto, che è una proprietà fondamentale degli insiemi.

B∩B**c=∅ rappresenta l'intersezione tra l'insieme B e il complemento dell'insieme B(B**c, che è uguale all'insieme vuoto 
B**c (complemento di B) rappresenta l'insieme complementare di B, ovvero l'insieme di tutti gli elementi presenti nell'insieme universo X che non sono in B.
L'intersezione tra un insieme B e il suo complemento B^c
  è l'insieme vuoto (∅), indicando che B e il suo complemento B^c
  sono insiemi disgiunti, ovvero non hanno alcun elemento in comune
'''
def calcola_intersezione_e_verifica_vuoto(B, universo):
    # Calcola il complemento di B rispetto all'insieme universo
    B_complemento = universo.difference(B)

    # Calcola l'intersezione tra B e il suo complemento
    intersezione = B.intersection(B_complemento)

    # Verifica se l'intersezione è l'insieme vuoto
    is_vuoto = (len(intersezione) == 0)

    return intersezione, is_vuoto

# Esempio di utilizzo
universo = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
B = {2, 4, 6, 8}

intersezione, is_vuoto = calcola_intersezione_e_verifica_vuoto(B, universo)

print("Intersezione tra B e il suo complemento:", intersezione)
print("L'intersezione è l'insieme vuoto?", is_vuoto)
