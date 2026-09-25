'''
Trova il limite dei perimetri dei poligoni regolari di n lati inscritti nel cerchio di raggio R e circoscritti intorno ad esso, quando n -> ∞

Quando n tende all'infinito, il poligono regolare si avvicina sempre di più a una circonferenza, e il limite del perimetro di questi poligoni sarà uguale al perimetro della circonferenza (2 * π * R).

In termini matematici:

Limite dei perimetri dei poligoni regolari quando n tende a infinito:
lim (n → ∞) Perimetro = 2 * π * R

Quindi, il limite dei perimetri dei poligoni regolari inscritti nel cerchio di raggio R e circoscritti intorno ad esso, quando il numero di lati n tende a infinito, è semplicemente 2 * π * R, che è il perimetro della circonferenza di raggio R.

'''


import matplotlib.pyplot as plt
import math

def perimeter_of_regular_polygon(n, R):
    # Calcola il lato del poligono regolare usando la formula "lato = 2 * R * sin(pi/n)"
    side = 2 * R * math.sin(math.pi / n)
    
    # Calcola il perimetro del poligono regolare usando la formula "perimetro = n * lato"
    perimeter = n * side
    
    return perimeter

def main():
    R = float(input("Inserisci il raggio del cerchio: "))
    max_sides = int(input("Inserisci il numero massimo di lati del poligono (ad esempio, 1000): "))

    n_values = range(3, max_sides + 1)
    perimeters = [perimeter_of_regular_polygon(n, R) for n in n_values]

    # Disegna il grafico del perimetro dei poligoni regolari in funzione del numero di lati
    plt.plot(n_values, perimeters)
    plt.axhline(2 * math.pi * R, color='r', linestyle='--', label='2πR (Circonferenza)')
    plt.xlabel('Numero di lati (n)')
    plt.ylabel('Perimetro')
    plt.title(f"Perimetro dei poligoni regolari inscritti e circoscritti alla circonferenza di raggio R = {R}")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()

'''
verrà visualizzato un grafico che rappresenta come il perimetro dei poligoni regolari si avvicina progressivamente al valore di 2πR (il perimetro della circonferenza) al crescere di "n". Il grafico dimostra il concetto matematico del limite dei perimetri dei poligoni regolari quando il numero di lati tende a infinito.
'''
