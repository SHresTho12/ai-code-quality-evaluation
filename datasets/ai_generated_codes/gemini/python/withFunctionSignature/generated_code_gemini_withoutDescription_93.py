
def encode(message):
  """Encodes a message into a list of numbers."""
  result = []
  for char in message:
    # Get the numeric code of the character.
    code = ord(char)
    # Convert the code to binary representation.
    binary = bin(code)[2:]
    # Add leading zeros to make all codes the same length.
    binary = binary.zfill(8)
    # Convert the binary string to a list of integers.
    result.extend([int(digit) for digit in binary])
  return result

# Example usage
message = "Hello, world!"
encoded_message = encode(message)
print(encoded_message)  # Output: [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
