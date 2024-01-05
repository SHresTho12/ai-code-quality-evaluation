
def is_simple_power(x, n):
  """
  This function checks if a number is a simple power of another number.

  Args:
      x: The number to be checked.
      n: The potential base of the power.

  Returns:
      True if x is a simple power of n, False otherwise.
  """

  if x <= 0 or n <= 0:
    return False

  # Check if x is divisible by n
  if x % n != 0:
    return False

  # Repeatedly divide x by n until it becomes 1
  while x > 1:
    x //= n

  # If x is now 1, it was a simple power of n
  return x == 1

# Example usage
number = 16
base = 2
if is_simple_power(number, base):
  print(f"{number} is a simple power of {base}")
else:
  print(f"{number} is not a simple power of {base}")
