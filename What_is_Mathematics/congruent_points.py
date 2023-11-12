import matplotlib.pyplot as plt
import numpy as np

def generate_congruent_points(num_points, x_range):
    # Genera punti x distribuiti in modo congruente
    x_points = np.linspace(-x_range, x_range, num_points)
    # Calcola i corrispondenti punti y sulla parabola (y = x^2)
    y_points = x_points ** 2
    return x_points, y_points

def plot_congruent_parabola(num_points, x_range):
    x_points, y_points = generate_congruent_points(num_points, x_range)

    plt.scatter(x_points, y_points, label='Congruent Points', color='blue')
    plt.plot(x_points, y_points, '--', color='red', label='Parabola (y = x^2)')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Parabola with Congruent Points')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    num_points = 100  # Numero di punti sulla parabola
    x_range = 10.0  # Intervallo sull'asse x
    plot_congruent_parabola(num_points, x_range)
