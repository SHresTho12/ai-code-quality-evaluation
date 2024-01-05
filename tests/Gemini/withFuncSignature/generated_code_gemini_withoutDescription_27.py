
def flip_case(string: str) -> str:
  """
  Flips the case of each character in a string.

  Args:
      string: The string to be flipped.

  Returns:
      A new string with the case of each character flipped.

  Notes:
      - Uppercase letters become lowercase, and vice versa.
      - Non-alphabetic characters are not affected.

  """

  flipped_string = ""
  for char in string:
    if char.isupper():
      flipped_string += char.lower()
    elif char.islower():
      flipped_string += char.upper()
    else:
      flipped_string += char

  return flipped_string

# Example usage
test_string = "Hello, World!"
flipped_string = flip_case(test_string)
print(f"Original string: {test_string}")
print(f"Flipped case: {flipped_string}")

METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(flip_case): 
    assert flip_case('') == '' 
    assert flip_case('Hello!') == 'hELLO!' 
    assert flip_case('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS' 
    
check(flip_case)
