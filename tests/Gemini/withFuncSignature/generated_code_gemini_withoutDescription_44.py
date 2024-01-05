
def change_base(x: int, base: int):
  """
  Converts a decimal number to a string representation in a given base.

  Args:
      x: The decimal number to convert.
      base: The base to convert to (2-16).

  Returns:
      A string representing the number in the given base.
  """

  # Handle negative numbers
  if x < 0:
    sign = "-"
    x = abs(x)
  else:
    sign = ""

  # Initialize an empty string to store the converted digits
  digits = ""

  # Loop until the number is 0
  while x > 0:
    # Get the remainder of dividing by the base
    remainder = x % base

    # Convert the remainder to a digit in the given base
    digit = "0123456789ABCDEF"[remainder]

    # Prepend the digit to the string
    digits = digit + digits

    # Divide the number by the base for the next iteration
    x //= base

  # Add the sign if necessary
  return sign + digits

# Example usage
print(change_base(10, 2))  # Output: 1010
print(change_base(255, 16))  # Output: FF
print(change_base(-123, 8))  # Output: -173


METADATA = {} 
def check(change_base): 
    assert change_base(8, 3) == "22" 
    assert change_base(9, 3) == "100" 
    assert change_base(234, 2) == "11101010" 
    assert change_base(16, 2) == "10000" 
    assert change_base(8, 2) == "1000" 
    assert change_base(7, 2) == "111" 
    for x in range(2, 8): 
        assert change_base(x, x + 1) == str(x) 
        
check(change_base)