import numpy as np

def nearest_neighbour(cities):
    num_cities = len(cities)
    unvisited_cities = set(range(num_cities))
    tour = [0]  # Inizia dalla città 0

    while len(unvisited_cities) > 1:
        current_city = tour[-1]
        nearest_city = min(unvisited_cities, key=lambda city: cities[current_city][city])
        tour.append(nearest_city)
        unvisited_cities.remove(nearest_city)

    # Aggiungi l'ultima città rimasta
    tour.append(unvisited_cities.pop())

    return tour
