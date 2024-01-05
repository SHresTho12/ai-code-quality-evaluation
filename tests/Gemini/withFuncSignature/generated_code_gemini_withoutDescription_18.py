
def how_many_times(string: str, substring: str) -> int:
  """
  Counts the number of times a substring appears in a string.

  Args:
      string: The string to search in.
      substring: The substring to count occurrences of.

  Returns:
      An integer representing the number of times the substring appears in the string.

  Notes:
      - The function is case-sensitive.
  """

  count = 0
  # Loop through the string, starting at index 0.
  for i in range(len(string)):
    # Check if the substring starts at the current index.
    if string[i:].startswith(substring):
      count += 1
  return count

# Example usage
test_string = "The quick brown fox jumps over the lazy dog."
substring = "the"
occurrences = how_many_times(test_string, substring)
print(f"The substring '{substring}' appears {occurrences} times in the string.")


METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(how_many_times): 
    assert how_many_times('', 'x') == 0 
    assert how_many_times('xyxyxyx', 'x') == 4 
    assert how_many_times('cacacacac', 'cac') == 4 
    assert how_many_times('john doe', 'john') == 1 
    
check(how_many_times)