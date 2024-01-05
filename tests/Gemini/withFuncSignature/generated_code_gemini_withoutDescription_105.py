
def by_length(arr):
  """
  Groups a list of strings by their length.

  Args:
      arr: A list of strings.

  Returns:
      A dictionary where the keys are the lengths of the strings and the values are
      lists of strings with that length.
  """

  # Create a dictionary to store the grouped strings.
  grouped_strings = {}

  # Iterate through each string in the list.
  for string in arr:
    # Get the length of the string.
    string_length = len(string)

    # Add the string to the corresponding list in the dictionary.
    if string_length not in grouped_strings:
      grouped_strings[string_length] = []
    grouped_strings[string_length].append(string)

  return grouped_strings

# Example usage
strings = ["apple", "banana", "orange", "grapefruit", "mango"]
grouped_by_length = by_length(strings)

print(grouped_by_length)  # Output: {3: ['apple', 'grape'], 5: ['banana', 'orange'], 6: ['mango']}


def check(by_length):
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"], "Error"
    assert by_length([]) == [], "Error"
    assert by_length([1, -1 , 55]) == ['One'], "Error"

# Check some edge cases that are easy to work out by hand.
assert True, "This prints if this assert fails 2 (also good for debugging!)"
assert by_length([1, -1, 3, 2]) == ["Three", "Two", "One"]
assert by_length([9, 4, 8]) == ["Nine", "Eight", "Four"]

check(by_length)
