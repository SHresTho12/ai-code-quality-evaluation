
import math

def triangle_area(a, b, c):
    """Calculates the area of a triangle using Heron's formula.

    Args:
        a: The length of the first side of the triangle.
        b: The length of the second side of the triangle.
        c: The length of the third side of the triangle.

    Returns:
        The area of the triangle.

    Raises:
        ValueError: If the input values do not form a valid triangle.
    """

    # Ensure triangle inequality holds for valid sides
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("Invalid triangle sides: lengths must satisfy the triangle inequality")

    # Calculate the semi-perimeter
    s = (a + b + c) / 2

    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return area
