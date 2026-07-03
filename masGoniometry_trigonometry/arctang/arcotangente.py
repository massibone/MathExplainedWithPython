import matplotlib.pyplot as plt
import numpy as np

def arctan(x, num_terms=1000):
    result = 0.0

    for n in range(num_terms):
        coefficient = (-1) ** n
        numerator = x ** (2 * n + 1)
        denominator = 2 * n + 1
        term = coefficient * (numerator / denominator)
        result += term

    return result

def plot_arctan(start_x, end_x, num_points):
    x_values = np.linspace(start_x, end_x, num_points)
    arc_tan_values = [arctan(x) for x in x_values]

    plt.plot(x_values, arc_tan_values, label="Arcotangente(x)")
    plt.xlabel("x")
    plt.ylabel("Arcotangente(x)")
    plt.title("Grafico dell'arcotangente di x")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    start_x = -1.0
    end_x = 1.0
    num_points = 100

    plot_arctan(start_x, end_x, num_points)
