
def triangle_area(a: float, h: float) -> float:
  """
  Calculates the area of a triangle given its base and height.

  Args:
      a: The base of the triangle (float).
      h: The height of the triangle (float).

  Returns:
      The area of the triangle (float).
  """

  # Formula for triangle area: 1/2 * base * height
  return 0.5 * a * h

# Example usage
area = triangle_area(5, 10)
print(f"Area of the triangle: {area}")  # Output: Area of the triangle: 25.0



METADATA = {} 
def check(triangle_area): 
    assert triangle_area(5, 3) == 7.5 
    assert triangle_area(2, 2) == 2.0 
    assert triangle_area(10, 8) == 40.0 
    
    
check(triangle_area)