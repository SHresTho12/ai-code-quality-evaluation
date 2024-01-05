
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
