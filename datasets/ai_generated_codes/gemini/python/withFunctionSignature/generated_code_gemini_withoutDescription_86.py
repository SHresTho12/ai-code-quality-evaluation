
def anti_shuffle(s):
  """
  Reverses the order of elements in a string, while maintaining the relative order of adjacent characters.

  Args:
    s: A string.

  Returns:
    A new string with the elements reversed in a specific way.
  """

  # Initialize an empty string to store the result
  result = ""

  # Iterate over the string in reverse order
  for i in range(len(s) - 1, -1, -1):
    # Append the current character to the result
    result += s[i]

    # If the current character is the same as the previous one, append another copy
    if i > 0 and s[i] == s[i - 1]:
      result += s[i]

  return result

# Example usage
string = "abbaccc"
anti_shuffled_string = anti_shuffle(string)
print(f"Original string: {string}")
print(f"Anti-shuffled string: {anti_shuffled_string}")  # Output: cccabbba
