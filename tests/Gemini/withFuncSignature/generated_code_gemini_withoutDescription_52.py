
def below_threshold(l: list, t: int) -> list:
  """
  Filters a list to only include elements below a given threshold.

  Args:
      l: The list to filter (list).
      t: The threshold value (int).

  Returns:
      A new list containing only elements from the original list that are below the threshold (list).
  """

  return [element for element in l if element < t]

# Example usage
my_list = [5, 10, 3, 7, 2, 8]
filtered_list = below_threshold(my_list, 5)
print(f"Original list: {my_list}")
print(f"List with elements below 5: {filtered_list}")


METADATA = {}

def check(below_threshold):
    assert below_threshold([1, 2, 4, 10], 100)
    assert not below_threshold([1, 20, 4, 10], 5)
    assert below_threshold([1, 20, 4, 10], 21)
    assert below_threshold([1, 20, 4, 10], 22)
    assert below_threshold([1, 8, 4, 10], 11)
    assert not below_threshold([1, 8, 4, 10], 10)

check(below_threshold)
