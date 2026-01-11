import math

# Costanti globali
GRAVITATIONAL_ACCELERATION = 9.81
PROJECTILE = "∙"
x_axis_tick = "T"
y_axis_tick = "⊣"

class Projectile:
    """
    Gestisce i calcoli fisici e le coordinate per un proiettile.
    """
    __slots__ = ('__speed', '__height', '__angle')

    def __init__(self, speed, height, angle):
        self.__speed = speed
        self.__height = height
        self.__angle = math.radians(angle) # Converte l'angolo in radianti
       
    def __str__(self):
        """Restituisce i dettagli del proiettile in formato leggibile."""
        return f'''
Projectile details:
speed: {self.speed} m/s
height: {self.height} m
angle: {self.angle}°
displacement: {round(self.__calculate_displacement(), 1)} m
'''

    def __calculate_displacement(self):
        """Calcola lo spostamento orizzontale massimo (punto d'impatto)."""
        horizontal_component = self.__speed * math.cos(self.__angle)
        vertical_component = self.__speed * math.sin(self.__angle)
        squared_component = vertical_component**2
        gh_component = 2 * GRAVITATIONAL_ACCELERATION * self.__height
        sqrt_component = math.sqrt(squared_component + gh_component)
       
        # Formula del dislocamento (range) per proiettili lanciati da un'altezza h
        return horizontal_component * (vertical_component + sqrt_component) / GRAVITATIONAL_ACCELERATION
       
    def __calculate_y_coordinate(self, x):
        """Calcola la coordinata Y per una data coordinata X."""
        height_component = self.__height
        angle_component = math.tan(self.__angle) * x
        acceleration_component = GRAVITATIONAL_ACCELERATION * x ** 2 / (
                2 * self.__speed ** 2 * math.cos(self.__angle) ** 2)
        y_coordinate = height_component + angle_component - acceleration_component

        return y_coordinate
   
    def calculate_all_coordinates(self):
        """
        Calcola e restituisce tutte le coordinate (x, y) del proiettile.
        Si ferma al dislocamento massimo arrotondato per eccesso.
        """
        max_displacement = math.ceil(self.__calculate_displacement())
        return [
            (x, self.__calculate_y_coordinate(x))
            for x in range(max_displacement)
        ]

    # Proprietà (getter)
    @property
    def height(self):
        return self.__height

    @property
    def angle(self):
        return round(math.degrees(self.__angle))

    @property
    def speed(self):
        return self.__speed

    # Setter (per la mutabilità)
    @height.setter
    def height(self, n):
        self.__height = n

    @angle.setter
    def angle(self, n):
        self.__angle = math.radians(n)

    @speed.setter
    def speed(self, s):
       self.__speed = s
   
    def __repr__(self):
        return f'{self.__class__}({self.speed}, {self.height}, {self.angle})'

class Graph:
    """
    Gestisce la visualizzazione delle coordinate in una tabella e un grafico ASCII.
    """
    __slots__ = ('__coordinates',)

    def __init__(self, coord):
        self.__coordinates = coord

    def __repr__(self):
        return f"Graph({repr(self.__coordinates)})"

    def create_coordinates_table(self):
        """Crea una tabella formattata delle coordinate (x, y)."""
        table = '\n  x      y\n'
        for x, y in self.__coordinates:
            # Formattazione stretta richiesta dal test
            table += f'{x:>3d}   {y:>3.2f}\n'

        return table

    def create_trajectory(self):
        """
        Crea e restituisce il grafico della traiettoria come una singola stringa multilinea.
        """
        rounded_coords = [(round(x), round(y)) for x, y in self.__coordinates]

        if not rounded_coords:
            return "\n\n" # Gestione caso vuoto

        # Trova le dimensioni massime per la matrice
        x_max = max(rounded_coords, key=lambda i: i[0])[0]
        y_max = max(rounded_coords, key=lambda j: j[1])[1]

        # Inizializza la matrice (lista di liste) di dimensioni (y_max+1) x (x_max+1)
        matrix_list = [[" " for _ in range(x_max + 1)] for _ in range(y_max + 1)]

        # Popola la matrice con il simbolo del proiettile, invertendo l'asse Y
        for x, y in rounded_coords:
            # L'indice di riga invertito per mappare il grafico cartesiano:
            row_index = y_max - y
           
            # Controlla i limiti per sicurezza (sebbene i dati siano già entro i limiti)
            if 0 <= row_index <= y_max and 0 <= x <= x_max:
                matrix_list[row_index][x] = PROJECTILE

        # 1. Unisce le liste interne (righe) in singole stringhe e antepone l'asse Y
        final_trajectory_list = [y_axis_tick + "".join(row) for row in matrix_list]

        # 2. Crea la riga dell'asse X
        x_axis_row = " " + x_axis_tick * (x_max + 1)
       
        # 3. Aggiunge la riga dell'asse X
        final_trajectory_list.append(x_axis_row)

        # 4. Unisce la lista di stringhe in una singola stringa multilinea,
        # aggiungendo \n all'inizio e alla fine.
        return "\n" + "\n".join(final_trajectory_list) + "\n"

def projectile_helper(speed, height, angle):
    """
    Funzione di utilità per creare un proiettile, calcolare la traiettoria e stamparne i dettagli,
    la tabella delle coordinate e il grafico.
    """
    # 1. Crea il proiettile
    ball = Projectile(speed, height, angle)
   
    # 2. Stampa i dettagli
    print(ball)
   
    # 3. Calcola le coordinate
    coordinates = ball.calculate_all_coordinates()
   
    # 4. Crea l'istanza Graph
    graph = Graph(coordinates)
   
    # 5. Stampa la tabella delle coordinate
    print(graph.create_coordinates_table())
   
    # 6. Stampa il grafico della traiettoria
    print(graph.create_trajectory())

# Chiama la funzione di utilità con valori a scelta
if __name__ == "__main__":
    # Esempio di chiamata: Velocità 10 m/s, Altezza 3 m, Angolo 45°
    projectile_helper(10, 3, 45)
#oppure solo projectile_helper(10, 3, 45) 

