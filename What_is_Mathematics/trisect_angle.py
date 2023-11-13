import matplotlib.pyplot as plt
import numpy as np

def trisect_angle(angle_A, plot=True):
    # Impostiamo la lunghezza del raggio del compasso
    radius = 1.0

    # Punto iniziale (centro del compasso)
    x_center, y_center = 0, 0

    # Punto A sulla circonferenza del compasso
    x_A = radius * np.cos(np.radians(angle_A))
    y_A = radius * np.sin(np.radians(angle_A))

    # Punto B sulla circonferenza del compasso
    angle_B = angle_A + 120  # Angolo trisezionato
    x_B = radius * np.cos(np.radians(angle_B))
    y_B = radius * np.sin(np.radians(angle_B))

    # Punto C sulla circonferenza del compasso
    angle_C = angle_A + 240  # Angolo trisezionato
    x_C = radius * np.cos(np.radians(angle_C))
    y_C = radius * np.sin(np.radians(angle_C))

    if plot:
        # Disegna l'arco e i punti A, B e C
        circle = plt.Circle((x_center, y_center), radius, fill=False)
        plt.plot([x_A, x_B, x_C, x_A], [y_A, y_B, y_C, y_A], label='Arco')
        plt.plot(x_A, y_A, 'ro', label='Punto A')
        plt.plot(x_B, y_B, 'go', label='Punto B')
        plt.plot(x_C, y_C, 'bo', label='Punto C')
        plt.xlim(-radius, radius)
        plt.ylim(-radius, radius)
        plt.gca().add_artist(circle)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axis('equal')
        plt.legend()
        plt.title('Trisezione dell\'angolo')
        plt.show()

    return (x_B, y_B), (x_C, y_C)

if __name__ == "__main__":
    angle_A = 60  # Angolo da trisectare (in gradi)
    point_B, point_C = trisect_angle(angle_A)
    print("Coordinate Punto B:", point_B)
    print("Coordinate Punto C:", point_C)
