
def count_distinct_characters(string: str) -> int:
  """
  This function counts the number of distinct characters in a string.

  Args:
      string: The string to analyze.

  Returns:
      An integer representing the number of distinct characters in the string.
  """

  # Create a set to store the unique characters.
  unique_chars = set()

  # Iterate over each character in the string.
  for char in string:
    # Add the character to the set if it is not already present.
    unique_chars.add(char)

  # Return the number of elements in the set (number of unique characters).
  return len(unique_chars)

# Example usage
test_string = "Hello, world!"
distinct_chars = count_distinct_characters(test_string)
print(f"The string '{test_string}' has {distinct_chars} distinct characters.")


METADATA = { 'author': 'jt', 'dataset': 'test' } 

def check(count_distinct_characters): 
    assert count_distinct_characters('') == 0 
    assert count_distinct_characters('abcde') == 5 
    assert count_distinct_characters('abcde' + 'cade' + 'CADE') == 5 
    assert count_distinct_characters('aaaaAAAAaaaa') == 1 
    assert count_distinct_characters('Jerry jERRY JeRRRY') == 5 
    
check(count_distinct_characters)