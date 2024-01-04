
def same_chars(s0: str, s1: str) -> bool:
  """
  Checks if two strings have the same characters, regardless of order.

  Args:
      s0: The first string (str).
      s1: The second string (str).

  Returns:
      True if the strings have the same characters, False otherwise (bool).
  """

  # Convert both strings to lowercase and remove whitespace
  s0_lower = s0.lower().replace(" ", "")
  s1_lower = s1.lower().replace(" ", "")

  # Create sets from the characters in each string
  s0_set = set(s0_lower)
  s1_set = set(s1_lower)

  # Check if the sets are equal
  return s0_set == s1_set

# Example usage
string1 = "Hello world!"
string2 = "dlrow olleH!"

if same_chars(string1, string2):
  print("The strings have the same characters.")
else:
  print("The strings do not have the same characters.")
