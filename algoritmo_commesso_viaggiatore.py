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

# Esempio di utilizzo

cities_coordinates = np.array([
    [0, 0],  # Città 0
    [1, 2],  # Città 1
    [3, 1],  # Città 2
    [5, 2]   # Città 3
])

tour = nearest_neighbour(cities_coordinates)
print("Tour ottimizzato:", tour)

