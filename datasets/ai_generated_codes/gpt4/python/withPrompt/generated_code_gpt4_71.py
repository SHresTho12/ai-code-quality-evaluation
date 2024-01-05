def triangle_area(a, b, c):
    """
    Calculate the area of a triangle given the lengths of its three sides.

    Args:
    a (float): Length of the first side.
    b (float): Length of the second side.
    c (float): Length of the third side.

    Returns:
    float: The area of the triangle rounded to 2 decimal points if it's a valid triangle,
           otherwise -1.

    Examples:
    >>> triangle_area(3, 4, 5)
    6.00
    >>> triangle_area(1, 2, 10)
    -1
    """

    # Check if the given sides can form a valid triangle
    if a + b > c and a + c > b and b + c > a:
        # Calculate the semi-perimeter of the triangle
        s = (a + b + c) / 2
        # Calculate the area using Heron's formula
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return round(area, 2)
    else:
        return -1
