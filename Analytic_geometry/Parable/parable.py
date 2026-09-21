import matplotlib.pyplot as plt

y_cords = range(-20,20)
x_cords = [x*x for x in y_cords]

plt.scatter(x_cords, y_cords)
plt.show()