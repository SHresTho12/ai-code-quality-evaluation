def triangle_area(a, h):
    """
    Calculate the area of a triangle given the length of a side (a) and the height (h).

    Args:
    a (float): Length of one side of the triangle.
    h (float): Height of the triangle.

    Returns:
    float: The area of the triangle.

    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    area = 0.5 * a * h
    return area

# Example test
print(triangle_area(5, 3))  # Output: 7.5
