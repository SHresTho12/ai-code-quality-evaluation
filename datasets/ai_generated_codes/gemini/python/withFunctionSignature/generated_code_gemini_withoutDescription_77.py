
def iscube(a):
  """
  This function checks if a number is a perfect cube.

  Args:
      a: The number to be checked.

  Returns:
      True if a is a perfect cube, False otherwise.
  """

  if a < 0:
    return False

  # Check if the cube root of a is an integer
  cube_root = a ** (1/3)
  return abs(cube_root - round(cube_root)) < 1e-6

# Example usage
number = 27
if iscube(number):
  print(f"{number} is a perfect cube")
else:
  print(f"{number} is not a perfect cube")
