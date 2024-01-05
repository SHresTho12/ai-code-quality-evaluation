import math

def triangle_area(a, b, c):
    """
    Calculates the area of a triangle given the lengths of its sides.

    :param a: Length of side a.
    :param b: Length of side b.
    :param c: Length of side c.
    :return: The area of the triangle.
    """
    # Check for the validity of the triangle
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle sides")

    # Calculate the semi-perimeter
    s = (a + b + c) / 2

    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
