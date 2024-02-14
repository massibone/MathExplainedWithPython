"""
    Divide a line segment defined by two points (x1, y1) and (x2, y2) according to a given ratio.

    Parameters:
    x1, y1 : float
        Coordinates of the first point.
    x2, y2 : float
        Coordinates of the second point.
    ratio : float
        Ratio at which the segment is to be divided. For example, if ratio = 0.5, the segment will be divided
        into two equal parts. If ratio = 0.3, the segment will be divided such that the first part is 30% of
        the total length.

    Returns:
    tuple
        Coordinates of the point dividing the segment.
"""
def divide_segment(x1, y1, x2, y2, ratio):
  
    # Calculate the coordinates of the point dividing the segment
    x = (x1 + ratio * x2) / (1 + ratio)
    y = (y1 + ratio * y2) / (1 + ratio)
    return x, y

# Example usage:
x1, y1 = 1, 1  # Coordinates of the first point
x2, y2 = 4, 5  # Coordinates of the second point
ratio = 0.3    # Ratio at which the segment is to be divided

# Call the function
x_div, y_div = divide_segment(x1, y1, x2, y2, ratio)

print("Coordinates of the point dividing the segment:", (x_div, y_div))
