
def hex_key(num):
  """
  This function converts a decimal number to its hexadecimal representation with a specific format.

  Args:
      num: The decimal number to be converted.

  Returns:
      A string representing the hexadecimal key with the following format:
          - If the number is less than 16, it is prefixed with "0" and converted to hexadecimal.
          - If the number is greater than or equal to 16, it is converted to hexadecimal without any prefix.

  Raises:
      ValueError: If the number is negative.
  """

  if num < 0:
    raise ValueError("Number must be non-negative")

  hex_string = hex(num).upper()[2:]  # Remove "0x" prefix and convert to uppercase

  # Add leading "0" if necessary
  if len(hex_string) == 1:
    hex_string = "0" + hex_string

  return hex_string

# Example usage
number = 15
hex_key_value = hex_key(number)
print(f"Hex key for {number}: {hex_key_value}")
