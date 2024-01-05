
def decimal_to_binary(decimal):
  """
  This function converts a decimal number to its binary representation.

  Args:
      decimal: The decimal number to be converted.

  Returns:
      A string representing the binary equivalent of the decimal number.
  """

  if decimal == 0:
    return "0"

  binary_string = ""
  while decimal > 0:
    remainder = decimal % 2
    binary_string = str(remainder) + binary_string
    decimal //= 2

  return binary_string

# Example usage
decimal_number = 10
binary_representation = decimal_to_binary(decimal_number)
print(f"{decimal_number} in binary: {binary_representation}")
