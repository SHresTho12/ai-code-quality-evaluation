
def string_sequence(n: int) -> str:
  """
  This function generates a string sequence of the form "1 2 3 ... n".

  Args:
      n: An integer representing the length of the sequence.

  Returns:
      A string containing the sequence of numbers from 1 to n, separated by spaces.
  """

  if n == 0:
    return ""
  else:
    return f"{n} {string_sequence(n-1)}"

# Example usage
print(string_sequence(5))  # Output: "5 4 3 2 1"
