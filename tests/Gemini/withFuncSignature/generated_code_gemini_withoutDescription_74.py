
def total_match(lst1, lst2):
  """
  This function counts the total number of matching elements between two lists.

  Args:
      lst1: The first list.
      lst2: The second list.

  Returns:
      The total number of elements that appear in both lists.
  """

  count = 0
  for element in lst1:
    if element in lst2:
      count += 1

  return count

# Example usage
lst1 = [1, 2, 3, 4, 5]
lst2 = [2, 4, 6, 8]
total_matches = total_match(lst1, lst2)
print(f"Total matching elements: {total_matches}")


def check(total_match):
    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert total_match([], []) == []
    assert total_match(['hi', 'admin'], ['hi', 'hi']) == ['hi', 'hi']
    assert total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']
    assert total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']
    assert total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']
    assert total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']
    assert total_match(['hi', 'admin'], ['hI', 'hi', 'hii']) == ['hi', 'admin']

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert total_match([], ['this']) == []
    assert total_match(['this'], []) == []

check(total_match)
