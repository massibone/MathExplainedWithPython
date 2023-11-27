'''
Il Problema di Apollonio riguarda la determinazione delle tangenti a tre cerchi dati.
'''

import sympy as sp

def apollonius_tangents(circle1, circle2, circle3):
    # Costruire le equazioni delle tangenti
    x, y = sp.symbols('x y')
    eq1 = sp.Eq((x - circle1[0])**2 + (y - circle1[1])**2, circle1[2]**2)
    eq2 = sp.Eq((x - circle2[0])**2 + (y - circle2[1])**2, circle2[2]**2)
    eq3 = sp.Eq((x - circle3[0])**2 + (y - circle3[1])**2, circle3[2]**2)

    # Risolvere le equazioni
    tangent_points = sp.solve((eq1, eq2, eq3), (x, y))

    return tangent_points


import matplotlib.pyplot as plt
import numpy as np

def plot_circle(ax, center, radius):
    circle = plt.Circle(center, radius, fill=False, color='r')
    ax.add_artist(circle)

def plot_tangent(ax, circle, point):
    ax.plot([circle[0], point[0]], [circle[1], point[1]], '--k')

if __name__ == "__main__":
    circle1 = (0, 0, 2)
    circle2 = (4, 0, 3)
    circle3 = (2, 5, 2.5)

    tangent_points = apollonius_tangents(circle1, circle2, circle3)

    # Plot circles
    fig, ax = plt.subplots()
    plot_circle(ax, (circle1[0], circle1[1]), circle1[2])
    plot_circle(ax, (circle2[0], circle2[1]), circle2[2])
    plot_circle(ax, (circle3[0], circle3[1]), circle3[2])

    # Plot tangent points
    for point in tangent_points:
        plot_tangent(ax, (circle1[0], circle1[1]), point)
        plot_tangent(ax, (circle2[0], circle2[1]), point)
        plot_tangent(ax, (circle3[0], circle3[1]), point)

    # Set plot limits and labels
    ax.set_xlim(-5, 10)
    ax.set_ylim(-5, 10)
    ax.set_aspect('equal')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    plt.title('Tangenti ai tre cerchi')
    plt.grid(True)
    plt.show()
