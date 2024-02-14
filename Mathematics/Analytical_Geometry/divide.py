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
