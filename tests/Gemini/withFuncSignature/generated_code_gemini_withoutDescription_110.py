
def exchange(lst1, lst2):
  """
  This function exchanges the elements of two lists at the same index.

  Args:
      lst1: The first list.
      lst2: The second list.

  Returns:
      Two new lists with the elements exchanged.
  """

  # Check if the lists have the same length
  if len(lst1) != len(lst2):
    raise ValueError("Lists must be the same length")

  # Create new lists to store the exchanged elements
  new_lst1 = []
  new_lst2 = []

  # Loop through the lists and exchange elements at each index
  for i in range(len(lst1)):
    new_lst1.append(lst2[i])
    new_lst2.append(lst1[i])

  return new_lst1, new_lst2


def check(exchange):
    # Check some simple cases
    assert exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES", "Test 1"
    assert exchange([1, 2, 3, 4], [1, 5, 3, 4]) == "NO", "Test 2"
    assert exchange([1, 2, 3, 4], [2, 1, 4, 3]) == "YES", "Test 3"
    assert exchange([5, 7, 3], [2, 6, 4]) == "YES", "Test 4"
    assert exchange([5, 7, 3], [2, 6, 3]) == "NO", "Test 5"
    assert exchange([3, 2, 6, 1, 8, 9], [3, 5, 5, 1, 1, 1]) == "NO", "Test 6"

    # Check some edge cases that are easy to work out by hand.
    assert exchange([100, 200], [200, 200]) == "YES", "Test 7"

check(exchange)
