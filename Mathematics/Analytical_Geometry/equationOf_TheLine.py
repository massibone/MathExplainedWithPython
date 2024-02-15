def equation_of_line(x1, y1, x2, y2):
    """
    Find the equation of a line passing through two given points.
    Parameters:
    x1, y1 : float
        Coordinates of the first point.
    x2, y2 : float
        Coordinates of the second point.

    Returns: tuple Coefficients (m, b) of the line equation 
    y = mx + b.
    """
    # Calculate the slope (m)
    m = (y2 - y1) / (x2 - x1)
    
    # Calculate the y-intercept (b) using one of the points
    b = y1 - m * x1
    
    return m, b

# Example usage:
x1, y1 = 1, 2  # Coordinates of the first point
x2, y2 = 3, 4  # Coordinates of the second point

# Call the function to find the equation of the line
m, b = equation_of_line(x1, y1, x2, y2)

# Print the equation of the line
print("Equation of the line: y =", m, "x +", b)
